from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'cart.html$', views.carts),
]