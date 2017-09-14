from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'cart.html$', views.cartSum),
    # url(r'abc.html$', views.carts),
]