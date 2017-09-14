
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.


#判断用户是否登录,装饰器
def decorate(func):
    def inner(request):
        user_id = request.session.get('id')
        # 没有登录重定向到登录页
        if user_id is None:
            return JsonResponse({'error': '0', 'path': '/user/login/','cart_count':0})
        else:
            return func(request)
    return inner


# 列表点击加入购物车请求视图
@decorate
def addcart(request):

    user_id = request.session.get('id')
    dict = request.POST
    goods_id = dict.get('goods_id')
    count = dict.get('count')
    goods_list = CartInfo.objects.filter(user_id=user_id)
    exist = True
    for goods in goods_list:
        if goods.goods_id == int(goods_id):
            #　如果购物车存在这个商品，数量加一
            goods = CartInfo.objects.get(user_id=user_id,goods_id=int(goods_id))
            goods.count = goods.count + int(count)
            goods.save()
            exist = False
    if exist:
        cart = CartInfo()
        cart.goods_id = goods_id
        cart.count = int(count)
        cart.user_id = user_id
        cart.save()
    user_list = CartInfo.objects.filter(user_id=user_id)
    cart_num = 0
    for i in user_list:
        cart_num += i.count
    return JsonResponse({'error':'1','path':'#','cart_num':cart_num})

@decorate
def cart_num(request):
    user_id = request.session['id']
    user_list = CartInfo.objects.filter(user_id=user_id)
    cart_count = 0
    for i in user_list:
        cart_count += i.count
    return JsonResponse({'cart_count':cart_count})


def cartSum(request):
    user_id = request.session.get('id')
    if user_id is None:
        return redirect('/user/login/')
    else:
        goods = CartInfo.objects.filter(user_id=1)
        context = {'goods':goods,'title':'天天生鲜－购物车'}
        return render(request, 'tt_cart/cart.html', context)
