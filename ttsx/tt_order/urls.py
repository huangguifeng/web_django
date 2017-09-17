
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^tt_order/$',views.orderGoods),
    url(r'^refer_order/$',views.referOrder),
]
