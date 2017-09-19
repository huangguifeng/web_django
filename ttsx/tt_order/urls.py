
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^tt_order/$',views.orderGoods),
    url(r'^refer_order/$',views.referOrder),
    url(r"^lj/$",views.order_liji),
    url(r'^order_pay(\d+)/$',views.order_pay),
    url(r'^list(\d*)/$',views.fenye),
]
