"""projectcariorang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path , include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from cariorang import views as cariorang_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',accounts_views.homeawal,name="homeawal"),
    path('home/',cariorang_views.PostCariView.as_view(template_name="home.html"), name="home"),
    path('search/',cariorang_views.SearchPostCari,name="search_hilang"),
    path('signup/',accounts_views.signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('reset/',auth_views.PasswordResetView.as_view(
        template_name = "password_reset.html",
        email_template_name = "password_reset_email.html",
        subject_template_name = "password_reset_subject.txt"),
        name="password_reset"),
    path('reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
        name="password_reset_done"),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm"),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
        name="password_reset_complete"),
    path('settings/password/',auth_views.PasswordChangeView.as_view(template_name="password_change.html"),
        name="password_change"),
    path('settings/password/done/',auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),
        name="password_change_done"),
    path('settings/my_account',accounts_views.update_profile,name="my_account"),
    path('formcari/',cariorang_views.BuatPostCari, name="formcari"),
    path('postcari/mypost/',cariorang_views.mypost,name="mypost"),
    re_path(r'postcari/(?P<pk>\d+)/$',cariorang_views.postcari_details.as_view(template_name="post_details.html"), name="post_details"),
    re_path(r'postcari/(?P<pk>\d+)/reply/$',cariorang_views.reply_comment, name="reply_comment"),
    re_path(r'postcari/(?P<pk>\d+)/details/(?P<pk_detail>\d+)/edit/$',cariorang_views.DetailUpdateView.as_view(template_name="edit_details.html"),name="edit_details"),
    re_path(r'postcari/(?P<pk>\d+)/post_edit',cariorang_views.PostCariUpdateView.as_view(template_name="edit_postcari.html"),name="edit_postcari"),
    re_path(r'postcari/(?P<pk>\d+)/delete_postcari/$',cariorang_views.PostCariDeleteView.as_view(template_name="delete_postcari.html"),name="delete_postcari"),
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    re_path(r'ketemu/(?P<pk>\d+)',cariorang_views.ketemu_diterima,name="ketemu"),
    re_path(r'cariorang/pdf/(?P<pk>\d+)',cariorang_views.template_cariorang , name="template_pdf"),
    path('dpo/', include('dpo.urls',namespace="dpo")),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
