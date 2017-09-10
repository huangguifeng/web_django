from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index),
    url(r'^list(\d+)/$',views.list),
    url('^admin/$',views.admin),
]