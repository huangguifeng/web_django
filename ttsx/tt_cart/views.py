from django.shortcuts import render

# Create your views here.

def carts(request):
    return render(request, 'tt_cart/cart.html')
