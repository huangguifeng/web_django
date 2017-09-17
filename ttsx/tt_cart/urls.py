from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.cartSum),
    url(r"^addcart/$",views.addcart),
    url(r'^cart_num/$',views.cart_num),
    url(r'^cart_del/$',views.cart_del),
    url(r'^cart_add/$',views.cart_add)
    # url(r'abc.html$', views.carts),
]