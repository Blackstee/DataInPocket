

from django.contrib import admin
from django.urls import path
from dip_manager import views
"""""
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name = 'register' ),
    #path('login', views.login, name = 'login' ),
    path('error', views.error, name = 'error' ),
    path('suggest', views.suggest, name = 'suggest' ),
    path(r'^login/$', auth_views.login, name='login'),
    path(r'^logout/$', auth_views.logout, name='logout'),
    path(r'^admin/', admin.site.urls),
]"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^tasks', views.tasks, name='home'),
    url(r'^task/(?P<id>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task/delete/(?P<id>[0-9]+)/$', views.task_delete, name='task_delete'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name= 'login.html'), name='logout'),
    url('admin_changes', TemplateView.as_view(template_name='admin_changes.html'), name='changes'),
    url('projects', views.projects, name='projects'),
    url(r'^project/(?P<id>[0-9]+)/$', views.proj_detail, name='proj_detail'),
    url(r'^project/delete/(?P<id>[0-9]+)/$', views.proj_delete, name='proj_delete'),
    url('users', views.users, name='users'),
    url(r'^user/(?P<id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^user/delete/(?P<id>[0-9]+)/$', views.user_delete, name='user_delete'),
    url(r'^account', views.account, name='account'),

#    url('error', views.error, name = 'error' ),
#   url('suggest', views.suggest, name = 'suggest' ),


]

