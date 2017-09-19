from django.shortcuts import render,redirect
from django.http import HttpResponse
from  tt_cart.models import CartInfo
from tt_goods.models import GoodsInfo
from tt_user.models import UserInfo, UserAddressInfo
from .models import *
from datetime import datetime
from django.db import transaction
from django.core.paginator import Paginator,Page
from tt_user.user_decorators import *
# Create your views here.

# 老师的方法
@is_login
def orderGoods(request):
    dict=request.GET
    cid=dict.getlist('cid')
    cart_list=CartInfo.objects.filter(goods_id__in=cid)
    userOby=UserInfo.users.get(id=request.session['id'])
    user=UserAddressInfo.objects.filter(user_id=userOby.id).order_by("-id")[0]

    context={'clist':cart_list,'user':user}

    return render(request,'tt_order/place_order.html',context)

@is_login
@transaction.atomic
def referOrder(request):
    try:
        cid=request.POST.getlist('cid')
        address=request.POST.get('address')

        #开启事务
        sid=transaction.savepoint()
        #创建订单主表
        order=OrderInfo()
        order.oid='%s%s'%(datetime.now().strftime('%Y%m%d%H%M%S'),'1')
        order.odate=datetime.now()
        user_id = request.session['id']  #+++++++++++++++
        order.user_id = user_id  #++++++++++++++
        # order.user_id=2   #---------------------
        order.ototal=0
        order.oaddress=address
        order.save()

        # 查询所有订单列表信息
        # orderinfo = OrderInfo.objects.filter(user_id=id). order_by('-oid')  #---------
        # orderinfo = OrderInfo.objects.filter(user_id=2).order_by('-oid')  # -------

        #查询选中的购物车信息，逐个遍历
        cart_list=CartInfo.objects.filter(id__in=cid)
        total=0
        isOk=True
        for cart in cart_list:
            #判断商品库存是否满足当前购买数量
            if cart.count<=cart.goods.gkuncun:
                #库存量足够，可以购买
                detail=OrderDetailInfo()
                detail.order=order
                detail.goods=cart.goods
                detail.price=cart.goods.gprice
                detail.count=cart.count
                detail.save()
                #计算总价
                total+=detail.count*detail.price
                #更改库存数量
                cart.goods.gkuncun-=cart.count
                cart.goods.save()
                #删除购物车数据
                cart.delete()
            else:
                isOk=False
                break
        if isOk:
            #保存总价
            order.ototal=total+10
            order.save()


            transaction.savepoint_commit(sid)
            return redirect('/order/list1/')
        else:
            #订单失败，是转到购物车，再次修改数量
            transaction.savepoint_rollback(sid)
            return redirect('/cart/')

    except Exception as e:

        print('--++---------%s----------++---'%e)


# 点击立即购买转到订单页面
@is_login
def order_liji(request):
    # 开启事务
    sid = transaction.savepoint()
    user_id = request.session['id']
    dict = request.GET
    ljid = int(dict.get('goods_id'))
    ljnum = int(dict.get('goods_num'))
    user = UserAddressInfo.objects.filter(user_id=user_id).order_by('-id')[0]

    # 创建订单主表
    order = OrderInfo()
    order.oid = '%s%s' % (datetime.now().strftime('%Y%m%d%H%M%S'), '1')
    order.odate = datetime.now()

    order.user_id = user_id
    # order.user_id=2
    order.ototal = 0
    order.oaddress = user.uname + user.uaddress + user.uphone
    order.save()

    total = 0
    goods = GoodsInfo.objects.filter(id=ljid)

    if ljnum <= goods[0].gkuncun:
        # 库存量足够，可以购买
        detail = OrderDetailInfo()
        detail.order = order
        detail.goods_id = ljid
        detail.price = goods[0].gprice
        detail.count = ljnum
        detail.save()
        # 计算总价
        total += detail.count * detail.price
        # 更改库存数量
        goods[0].gkuncun -= detail.count
        goods[0].save()

        order.ototal = total + 10
        order.save()

        transaction.savepoint_commit(sid)
        return redirect('/order/list1/')

    else:
        # 订单失败，是转到购物车，再次修改数量
        transaction.savepoint_rollback(sid)
        return HttpResponse('商品库存不足')


def order_pay(request,dd):
    orderinfo=OrderInfo.objects.get(oid=dd)
    orderinfo.oIsPay=True
    orderinfo.save()
    context={'orderinfo':orderinfo}
    return render(request,'tt_order/order_pay.html',context)

def fenye(request,pindex):
    # 查询所有订单列表信息
    order = OrderInfo()
    uid = request.session.get('id')
    orderinfo = OrderInfo.objects.filter(user_id=uid).order_by('-oid')
    # orderinfo = OrderInfo.objects.filter(user_id=2).order_by('-oid')
    # 分页显示数据
    paginator = Paginator(orderinfo,4)
    pindex1 = int(pindex)
    page = paginator.page(pindex1)
    context = {'orderinfo': orderinfo,'page': page, 'pindex': pindex1,'oIsPay': order.oIsPay,'info':'用户中心','title':'天天生鲜－我的订单'}
    return render(request, 'tt_user/user_center_order.html', context)






# 我的方法
# def orderGoods(request):
#
#     goodsList=[]
#     user_id=2 #---------
#
#     #  获取用户的id
#     # user_id = request.session['id'] #++++++++
#     user_id = int(user_id)
#
#     # 获取编号为user_id的人的购物车对象
#     carMessage = CartInfo.objects.filter(user_id=user_id)
#     # 获取商品的信息
#     for i in carMessage:
#         # oneGoods=i.goods
#         goodsList.append(i)
#
#     context={'goodsList':goodsList}
#     return render(request,'tt_order/place_order.html',context)

# @transaction.atomic
# def referOrder(request):
#
#     try:
#         decide_nuber=[]
#
#         sid = transaction.savepoint()
#
#         # 用户id
#         # user_id = request.session['id']  #+++++++++++++++
#         user_id = 2  #---------
#
#         # 获取编号为user_id的人的购物车对象
#         carMessage = CartInfo.objects.filter(user_id=user_id)
#
#         # 目前（下单）时间
#         now = datetime.now()
#
#         # 获取当前顾客收货地址
#         address = UserAddressInfo.objects.get(user_id=user_id)
#         oaddress = address.uaddress
#
#         # 创建订单主表
#         order_info = OrderInfo()
#         order_info.oid='%s%d'%(now.strftime('%Y%m%d%H%M%S'),user_id) #订单编号
#         order_info.user_id=user_id #订单用户(id)
#         order_info.odate=now  # 下单日期
#         order_info.oIsPay=False   # 是否支付
#         order_info.ototal= 0  # 金额总计
#         order_info.oaddress=oaddress #收货地址
#         # order_info.save()  #+++++++++++++++++++
#         print(order_info.oaddress)
#
#         for ogoods in carMessage:   # 获取对应商品
#             goods_store = ogoods.goods.gkuncun  #库存
#             goods_count = ogoods.count         #购买数量
#             oprice = ogoods.goods.gprice
#             ocount = ogoods.count
#             # 判断库存是否充足
#             if int(goods_store) >= int(goods_count):
#                 ogoods.goods.gkucun=goods_store-goods_count
#                 # ogoods.goods.save()   #+++++++++++++++++++
#                 order_info.ototal+=oprice*ocount
#
#                 # 创建从表
#                 odetail = OrderDetailInfo()  # 从表对象
#                 odetail.goods_id=ogoods.goods_id
#                 odetail.order_id=order_info.oid
#                 odetail.price=oprice
#                 odetail.count=ocount
#                 # odetail.save()    #+++++++++++++++++++
#
#                 # 保存 主表内容
#                 # order_info.save()  #+++++++++++++++++++
#                 # 删除购物车对象
#                 # carMessage.delete()
#
#                 transaction.savepoint_commit(sid)
#                 # return HttpResponse('ok')
#                 return redirect('/user/center_order/')
#                 # return render(request,'tt_user/user_center_order.html')
#             else:
#                 # 回滚事件
#                 transaction.savepoint_rollback(sid)
#                 return redirect('/cart/')
#
#     except Exception as e:
#
#         #回滚事件
#         # transaction.savepoint_rollback(sid)
#         print('--++---------%s----------++---'%e)














