from django.urls import path , re_path
from dpo import views as dpo_views

app_name = 'dpo'

urlpatterns = [
    path('home/',dpo_views.DPOView.as_view(template_name="dpo_home.html"),name="home"),
    path('formcaridpo/',dpo_views.BuatFormDPO, name="formcaridpo"),
    path('search/',dpo_views.SearchPostDPO,name="search_dpo"),
    re_path(r'postdpo/mypostdpo/',dpo_views.mypostdpo, name="mypostdpo"),
    re_path(r'postdpo/(?P<pk>\d+)/$',dpo_views.postdpo_details.as_view(template_name="post_details_dpo.html"),name="post_details_dpo"),
    re_path(r'postdpo/(?P<pk>\d+)/reply/$',dpo_views.reply_comment, name="reply_comment"),
    re_path(r'postdpo/(?P<pk>\d+)/detailsdpo/(?P<pk_details>\d+)/edit/$',dpo_views.DetailUpdateView.as_view(template_name="edit_details_dpo.html"),name="edit_details_dpo"),
    re_path(r'postdpo/(?P<pk>\d+)/delete_postdpo/$',dpo_views.PostDPODeleteView.as_view(template_name="delete_postcari.html"),name="delete_postdpo"),
    re_path(r'postdpo/(?P<pk>\d+)/post_edit_dpo',dpo_views.PostDPOUpdateView.as_view(template_name="edit_postcari_dpo.html"),name="edit_postcari_dpo"),
    re_path(r'caridpo/pdf/(?P<pk>\d+)',dpo_views.template_caridpo , name="template_pdf_dpo"),



]
