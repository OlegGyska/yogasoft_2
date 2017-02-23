from django.views.generic import TemplateView, ListView, DetailView, FormView
from os.path import join, abspath
from datetime import date
from os import mkdir
from .forms import *


class MainPage(TemplateView):
    template_name = 'base.html'


class StartProjectView(FormView):
    template_name = "base.html"
    form_class = StartProjectForm
    success_url = "/app/"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')

        if form.is_valid():
            data = form.cleaned_data
            pth = join('stor', str(date.today()) + '-' + data['first_name'] + '-' + data['last_name'])
            try:
                mkdir(pth)
            except FileExistsError:
                pass
            form.cleaned_data['file'] = abspath(pth)
            for f in files:
                with open(join(pth, str(f)), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            return self.form_valid(form, abspath(pth))
        else:
            return self.form_invalid(form)

    def form_valid(self, form, pth):

        a = form.save(commit=False)
        a.file = pth
        a.save()

        return super(StartProjectView, self).form_valid(form)
