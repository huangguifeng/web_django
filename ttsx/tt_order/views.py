from django.shortcuts import render,HttpResponse
from django.utils.datetime_safe import strftime

from tt_cart.models import CartInfo
from tt_user.models import UserInfo
from .models import *
from datetime import datetime

# Create your views here.


def orderGoods(request):

    goodsList=[]
    user_id=2 #---------

    #  获取用户的id
    # user_id = request.session['user_id'] #++++++++
    user_id = int(user_id)

    # 获取编号为user_id的人的购物车对象
    carMessage = CartInfo.objects.filter(user_id=user_id)

    # 获取商品的信息
    for i in carMessage:
        # oneGoods=i.goods
        goodsList.append(i)

    context={'goodsList':goodsList}
    return render(request,'tt_order/place_order.html',context)


def referOrder(request):

    try:
        decide_number = []
        user_id = 2  #---------
        # 获取编号为user_id的人的购物车对象
        carMessage = CartInfo.objects.filter(user_id=user_id)

        # 创建订单主表
        order_info = OrderInfo()
        # order_info.oid=

        # 获取对应商品库存
        for ogoods in carMessage:
            goods_store = ogoods.goods.gkucun
            goods_count = ogoods.count
            if int(goods_store) > int(goods_count):
                print('test')

    except Exception as e:
        print('-----------%s-------------'%e)

print('ok')
i=datetime.now()
print(i)
strftime('%Y%m%d%H%M%S'),













    #         decide_number.append(1)
    #     else:
    #         decide_number.append(0)
    # if 0 in decide_number:
    #     context={'decide_number':decide_number}
    #     return render(request,'tt_order/')
