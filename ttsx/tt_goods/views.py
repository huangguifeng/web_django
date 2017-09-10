from django.shortcuts import render
from .models import *
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
    context = {'Typelist':typelist,'list0':list0,
               'list01':list01,'list1':list1,'list11':list11,
               'list2':list2,'list21':list21,
               'list3':list3,'list31':list31,
               'list4':list4,'list41':list41,
               'list5':list5,'list51':list51}
    return render(request,'tt_goods/index.html',context)

def list(request,pindex):

    typelist = TypeInfo.objects.all()

    paginator = Paginator(typelist,15)
    page = paginator.page(int(pindex))
    context = {'typelist': page}
    return render(request,'tt_goods/list.html',context)


def admin(request):
    pass

