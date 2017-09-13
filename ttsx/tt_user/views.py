from hashlib import sha1

from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from tt_user.models import UserInfo
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont


# 注册
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
        upwd = user_info.get('cpwd')
        s1=sha1()
        s1.update(upwd.encode('utf-8'))
        upwd_sha1=s1.hexdigest()
        u_email = user_info.get('email')
        user = UserInfo.users.create_user(uname,upwd_sha1,u_email)
        user.save()
        msg = '<a href="http://127.0.0.1:8000/user/active%s/" target="_blank">点击激活</a>' %(user.id)
        send_mail('注册激活', '', settings.EMAIL_FROM,
                  [u_email],
                  html_message=msg)
        return HttpResponse('用户注册成功，请到邮箱中激活')

def active(request,uid):
    list = UserInfo.users.get(id=uid)
    list.isActive=True
    list.save()
    return HttpResponse('激活成功')
def abb (request):
    list = UserInfo.users.get(uname='admin1234')
    if list:
        return HttpResponse(list)
    else:
        return HttpResponse(list)

# 登录
def namech (request):
    na_me = request.GET.get('name')
    list = UserInfo.users.filter(uname=na_me)
    if list :
        return JsonResponse({'data': 1})
    else:
        return JsonResponse({'data': 0 })
def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 36
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    #内存文件操作(python2)
    #import cStringIO
    #buf = cStringIO.StringIO()

    #内存文件操作(python3)
    from io import BytesIO
    buf = BytesIO()

    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
def user_login(request):
    list=request.POST
    yzm=list['yzm']
    if yzm.lower()==request.session['verifycode'].lower():
        u_name=list['username']
        u_pwd=list['pwd']
        s1=sha1()
        s1.update(u_pwd.encode('utf-8'))
        obb=s1.hexdigest()
        ob=UserInfo.users.get(uname=u_name).upwd
        if obb==ob:
            response=render(request,'tt_goods/index.html')
            response.set_cookie('name',u_name)
            request.session['uname']=u_name
            return response
        else :
            context={'data':"alert('密码不正确请重新登录')"}
            return  render(request,'tt_user/login.html',context)
    else:
        context = {'data': "alert('验证码错误')","title":"天天生鲜-登录"}
        return render(request,'tt_user/login.html',context)

# 用户中心
def center_info(request):

    return render(request,'tt_user/user_center_info.html',{'title':'天天生鲜-用户中心'})
# def center_info (request):
#     return redirect('/tt_user/user_center_info.html')