from django.shortcuts import render
from tt_cart.models import *
from tt_goods.models import *
from django.http import HttpResponse

# Create your views here.

# def carts(request):
    # return render(request, 'tt_cart/abc.html', abc)

def cartSum(request):
    goods_obj = GoodsInfo.objects.filter(id__gt=26).filter(id__lt=31)
    goods = {'goods':goods_obj}
    return render(request, 'tt_cart/cart.html', goods)
