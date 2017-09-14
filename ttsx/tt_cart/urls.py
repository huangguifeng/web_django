from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.cartSum),
    url(r"^addcart/$",views.addcart),
    url(r'^cart_num/$',views.cart_num),


    # url(r'abc.html$', views.carts),
]