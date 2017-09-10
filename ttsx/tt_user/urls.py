from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^register/$',views.register),
    url(r'login/',views.login),
    url(r'verifycode/',views.verifycode),
    url(r'^code/$',views.code),
    url(r'^verify_user/',views.verify_user)
]