from django.conf.urls import include, url
from tt_user import views
from tt_user.requires_login import if_login
from tt_user.views import *

urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^namebj/$',views.namebj),
    url(r'^emailbj/$',views.emailbj),
    url(r'^active（\d+）/$',views.active),
    url(r'^create/',views.create),
    url(r'^abb/$',views.abb),
    url(r'^namech/$',views.namech),
    url(r'^user_login/$',views.user_login),
    url(r'^verify_code/',views.verify_code),
    url(r'^center_info/$',if_login(center_info)),
    url(r'^center_order/$',if_login(center_order)),
    url(r'^center_site/$', if_login(center_site)),
    url(r'^user_addr/$',views.user_addr),
    url(r'logout/$', views.logout),

]