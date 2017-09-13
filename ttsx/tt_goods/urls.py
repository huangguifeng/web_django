from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index),
    url(r'^list(\d+)_(\d+)/$',views.list),
    url('^admin/$',views.admin),
    url(r'^(\d+)/$',views.detail),
]