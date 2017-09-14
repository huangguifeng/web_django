from tt_cart.models import *
from tt_goods.models import *

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.


# 列表点击加入购物车请求视图
def addcart(request):

    user_id = request.session.get('id')
    # 没有登录重定向到登录页
    if user_id is None:
        return JsonResponse({'error':'0','path':'/user/login/'})
    else:
        dict = request.POST
        goods_id = dict.get('goods_id')
        goods_list = CartInfo.objects.filter(user_id=1)

        exist = True
        for goods in goods_list:
            if goods.goods_id == int(goods_id):
                #　如果购物车存在这个商品，数量加一
                goods = CartInfo.objects.get(user_id=user_id,goods_id=int(goods_id))
                goods.count = goods.count + 1
                goods.save()
                exist = False
        if exist:
            cart = CartInfo()
            cart.goods_id = goods_id
            cart.count = 1
            cart.user_id = user_id
            cart.save()
        user_list = CartInfo.objects.filter(user_id=user_id)
        cart_num = 0
        for i in user_list:
            cart_num += i.count
        return JsonResponse({'error':'1','path':'#','cart_num':cart_num})


def cart_num(request):
    # uid = request.session['id']
    user_list = CartInfo.objects.filter(user_id=1)
    cart_count = 0
    for i in user_list:
        cart_count += i.count
    return JsonResponse({'cart_count':cart_count})




# def carts(request):
    # return render(request, 'tt_cart/abc.html', abc)

def cartSum(request):

    user_list = CartInfo.objects.filter(user_id=1)
    goods_list = []
    for goods in user_list:
        goods_list.append(goods.goods_id)

    goods_obj = GoodsInfo.objects.filter(id__in=goods_list)
    goods = {'goods':goods_obj}


    return render(request, 'tt_cart/cart.html', goods)
