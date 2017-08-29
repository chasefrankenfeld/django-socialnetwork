from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login, password_reset
from . import views

urlpatterns = [
        url(r'^$', views.dashboard, name="dashboard"),
        # login / login urls
        url(r'^login/$', login, name='login'),
        url(r'^logout/$', logout, name='logout'),
        url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

        url(r'^password_reset/$', password_reset, name='password_reset'),
    ]
