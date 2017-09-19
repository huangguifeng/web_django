from django.shortcuts import render
from .models import *
# Create your views here.

# def carts(request):
#     return render(request, 'tt_cart/cart.html')
def carts(request):
    cart_list=CartInfo.objects.filter(user_id=2)#request.session['uid']
    context={'clist':cart_list}
    return render(request,'tt_cart/cart.html',context)