from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from tt_user.models import UserInfo
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

def register(request):

    title = '天天生鲜-注册'
    context = {"title":title}
    return render(request, 'tt_user/register.html', context)

def login(request):
    title = '天天生鲜-登录'
    context = {"title":title}
    return render(request, 'tt_user/login.html', context)
def namebj (request):
    name=request.GET.get('name')
    list=UserInfo.users.filter(uname=name)
    if list:
        return JsonResponse ({'data':0})
    else :
        return JsonResponse ({'data':1})


def emailbj (request):
    email = request.GET.get('email')
    list = UserInfo.users.filter(uemail=email)
    if list :
        return JsonResponse({'data': 0})
    else:
        return JsonResponse({'data': 1 })
def create (request):
    user_info=request.POST
    uname=user_info.get('user_name')
    list = UserInfo.users.filter(uname=uname)
    if list :
        return HttpResponse('注册失败')
    else:
        upwd = user_info.get('pwd')
        u_email = user_info.get('email')
        user = UserInfo.users.create_user(uname, upwd, u_email)
        user.save()
        msg = '<a href="http://127.0.0.1:8000/active/?u_email=%s" target="_blank">点击激活</a>' % u_email
        send_mail('注册激活', '', settings.EMAIL_FROM,
                  [u_email],
                  html_message=msg)
        return HttpResponse('ok')

def active(request):
    ff=request.GET
    u_email=ff.get('u_email')
    list = UserInfo.users.get(uemail=u_email)
    list.isActive=True
    list.save()
    return HttpResponse('激活')
def abb (request):
    list = UserInfo.users.filter(uname='admin34')
    if list:
        return HttpResponse('1')
    else:
        return HttpResponse('0')