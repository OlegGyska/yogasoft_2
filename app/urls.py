from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name="main_page"),
    url(r'^alt/$', views.AltPage.as_view(), name="alt"),

    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^registration$', views.register, name="registration"),
    url(r'^portfolio/$', views.PortfolioListView.as_view(), name="portfolio"),
    url(r'^portfolio/(?P<pk>\d+)', views.PortfolioDetailView.as_view(), name="portfolio_detail"),
    url(r'^index/$', views.IndexPage.as_view(), name="index_page"),
    url(r'^index$', views.IndexPage.as_view(), name="index_page"),
    url(r'^access_required/$', views.AccessRequired.as_view(), name='access_required_page'),
    url(r'start_project/$', views.StartProjectView.as_view(), name="start_project"),
    url(r'testimonials/$', views.Testimonials.as_view(), name="testimonials"),
    url(r'testimonials_admin/$', views.TestimonialsAdmin.as_view(), name="testimonials_admin"),
    url(r'testimonials_admin/(?P<testimonial_id>[0-9]+)/$', views.TestimonialsAdmin.as_view(),
        name="testimonials_admin"),
    url(r'^blog/(?P<pk>\d+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^blog/(?P<pk>\d+)/add_comment/(?P<comm_pk>\d+)/$', views.add_second_comment, name='add_second_level_comment'),
    url(r'^blog/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog_detail_view'),
    url(r'^blog/$', views.BlogListView.as_view(), name='blog_list_view'),
    url(r'^blog/tag/(?P<tag>[a-zA-Z0-9 ]+)/$', views.BlogListView.as_view(), name='blog_list_view_tag'),
    url(r'^site_admin/$', views.SiteAdmin.as_view(), name='site_admin'),
    url(r'^site_admin/admin_users/$', views.AdminUsers.as_view(), name='admin_users'),
    url(r'^site_admin/edit_admin_user/(?P<user_id>[0-9]+)/$', views.EditAdminUser.as_view(), name='edit_admin_user'),
    url(r'^site_admin/general_users/$', views.GeneralUsers.as_view(), name='general_users'),
    url(r'^site_admin/edit_general_user/(?P<user_id>[0-9]+)/$', views.EditGeneralUser.as_view(), name='edit_general_user'),
    url(r'^contact_us/$', views.ContactUsView.as_view(), name='contact_us'),
    url(r'^site_admin/contact_us_admin/$', views.ContactUsAdmin.as_view(), name='contact_us_admin'),
    url(r'^site_admin/contact_us_admin/(?P<cu_id>[0-9]+)/$', views.ContactUsAdmin.as_view(), name='contact_us_admin'),
    url(r'^contact_us_success/$', views.ContactUsSuccess.as_view(), name='contact_us_success'),
    url(r'^search_list/(?P<info>.*)$', views.SearchListAsView.as_view(), name='search'),
    url(r'^site_admin/blogs/$', views.AdminBlogList.as_view(), name='admin_blog_posts'),
    url(r'^site_admin/blogs/create/$', views.CreateBlogPost.as_view(), name='create_blog_post'),
    url(r'^site_admin/blogs/change/(?P<pk>\d+)/$', views.ChangeBlogPost.as_view(), name='change_blog_post'),
    url(r'^site_admin/blogs/delete/(?P<pk>\d+)/$', views.BlogPostDelete.as_view(), name='delete_blog_post'),
    url(r'^site_admin/projects/$', views.ProjectsListView.as_view(), name='projects_list'),
    url(r'^site_admin/projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_view'),
    url(r'^site_admin/projects/(?P<pk>\d+)/close/$', views.close_project, name='close_project'),
    url(r'^site_admin/projects/(?P<pk>\d+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),
    url(r'^site_admin/projects/(?P<pk>\d+)/download/all/$', views.project_all_files_download,
        name='project_files_download'),
    url(r'^site_admin/projects/(?P<pk>\d+)/download/(?P<file>\S+)/$', views.project_file_download,
        name='project_file_download'),
    url(r'^site_admin/portfolio/$', views.PortfolioAdminList.as_view(), name='portfolio_admin_list'),
    url(r'^site_admin/portfolio/create/$', views.CreatePortfolio.as_view(), name='create_portfolio'),
    url(r'^site_admin/portfolio/(?P<pk>\d+)/delete/$', views.PortfolioDelete.as_view(), name='portfolio_delete'),
    url(r'^site_admin/portfolio/change/(?P<pk>\d+)/$', views.ChangePortfolio.as_view(), name='change_portfolio'),
    url(r'^contact_us/$', views.ContactUsView.as_view(), name='contact_us'),
    url(r'^site_admin/comments/moderate/(?P<pk>\d+)/$', views.moderate_comment, name='comment_admin_moderate'),
    url(r'^site_admin/comments/moderate_sec/(?P<pk>\d+)/$', views.moderate_sec_comment,
        name='comment_admin_moderate_sec'),
    url(r'^site_admin/comments/delete/(?P<pk>\d+)/$', views.delete_comment, name='comment_admin_delete'),
    url(r'^site_admin/comments/delete_sec/(?P<pk>\d+)/$', views.delete_sec_comment, name='comment_admin_delete_sec'),
    url(r'^site_admin/comments/$', views.CommentsAdmin.as_view(), name='comment_admin'),
    url(r'^search_list/(?P<info>.*)$', views.SearchListAsView.as_view(), name='search'),
    url(r'^site_admin/tags/$', views.TagsAdmin.as_view(), name='tags_admin'),
    url(r'^site_admin/tags/(?P<tag_id>\d+)/$', views.TagsAdmin.as_view(), name='tags_admin'),
]
