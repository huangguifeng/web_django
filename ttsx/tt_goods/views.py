

from django.shortcuts import render
from tt_goods.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    typelist = TypeInfo.objects.all()
    list0 = typelist[0].goodsinfo_set.order_by("-id")[0:4]
    list01 = typelist[0].goodsinfo_set.order_by("gclick")[0:4]
    list1 = typelist[1].goodsinfo_set.order_by("-id")[0:4]
    list11 = typelist[1].goodsinfo_set.order_by("gclick")[0:4]
    list2 = typelist[2].goodsinfo_set.order_by("-id")[0:4]
    list21 = typelist[2].goodsinfo_set.order_by("gclick")[0:4]
    list3 = typelist[3].goodsinfo_set.order_by("-id")[0:4]
    list31 = typelist[3].goodsinfo_set.order_by("gclick")[0:4]
    list4 = typelist[4].goodsinfo_set.order_by("-id")[0:4]
    list41 = typelist[4].goodsinfo_set.order_by("gclick")[0:4]
    list5 = typelist[5].goodsinfo_set.order_by("-id")[0:4]
    list51 = typelist[5].goodsinfo_set.order_by("gclick")[0:4]
    context = {'tlist':typelist,'list0':list0,'title':"天天生鲜",
               'list01':list01,'list1':list1,'list11':list11,
               'list2':list2,'list21':list21,
               'list3':list3,'list31':list31,
               'list4':list4,'list41':list41,
               'list5':list5,'list51':list51}
    return render(request,'tt_goods/index.html',context)


def list(request,tid,pindex,sort):
    # 获取商品的类型，通过ｉｄ
    typelist = TypeInfo.objects.get(pk=int(tid))
    list = typelist.goodsinfo_set.order_by('-id')[0:2]

    if sort == '1':#默认的排序
        goodslist = GoodsInfo.objects.filter(gtype__id=int(tid)).order_by('id')
    if sort == '2':#按照价格排序
        goodslist = GoodsInfo.objects.filter(gtype__id=int(tid)).order_by('-gprice')
    if sort == '3':#按照点击量排序
        goodslist = GoodsInfo.objects.filter(gtype__id=int(tid)).order_by('-gclick')

    # 分页
    paginator = Paginator(goodslist,10)#一页多少个数据
    page = paginator.page(int(pindex))#分多少页
    context = {'goodslist': page,'list':list,"tid":tid,"sort":sort,
               "title":typelist.ttitle,'typelist':typelist}
    return render(request,'tt_goods/list.html',context)


def detail(request,gid):
    # 通过商品的id来获取商品
    goods = GoodsInfo.objects.get(pk=int(gid))
    goods.gclick +=1#点击量
    goods.save()
    # 获取每种类型的两种商品，-为倒序排序
    list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context ={'goods':goods,'list':list,'title':"商品详情"}
    respose =  render(request,'tt_goods/detail.html',context)

    # 获取用户最近的五个商品的浏览记录
    goods_id = request.COOKIES.get('goods_id')
    if goods_id != None:
        list = goods_id.split('/')#切割后list为一个列表
        if gid not in list:
            if len(list) >4:#保存五个数据
                del list[0]
                list.append(gid)
            else:
                list.append(gid)
        goodid = '/'.join(list)
        #拼接为字符串
        respose.set_cookie('goods_id',goodid)
    else:
        respose.set_cookie('goods_id',gid)
    return respose

# from haystack.views import SearchView

# class Search(SearchView):
#     def extra_context(self):
#         context = super(Search,self).extra_context()
#         context['title']='搜索'
#         context['cart_count']=list(self.request)
#         return context

def admin(request):
    pass


