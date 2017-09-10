from django.conf.urls import include, url
from tt_user import views

urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^namebj/$',views.namebj),
    url(r'^emailbj/$',views.emailbj),
    url(r'^active/$',views.active),
    url(r'^create/',views.create),
    url(r'^abb/$',views.abb)
]