from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
import random
from io import BytesIO
from .models import *
# Create your views here.

def register(request):

    title = '天天生鲜-注册'
    context = {"title":title}
    return render(request, 'tt_user/register.html', context)



def login(request):
    title = '天天生鲜-登录'
    context = {"title":title}
    return render(request, 'tt_user/login.html', context)



def verifycode(request):
    """随机生成6位的验证码（字母数字随机组合，包含大小写）"""

    code_list = []
    # 每一位验证码都有三种可能（大写字母，小写字母，数字）
    for i in range(6):
        statu = random.randint(1,3)
        if statu == 1:
            a = random.randint(65,90)
            random_uppercase = chr(a)
            code_list.append(random_uppercase)

        elif statu == 2:
            b = random.randint(97,122)
            random_lowercase = chr(b)
            code_list.append(random_lowercase)

        elif statu == 3:
            random_num = random.randint(0,9)
            code_list.append(str(random_num))

    verification_code = "".join(code_list)
    font = ImageFont.truetype('FreeMono.ttf', 23)  # 字体
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(10,255))
    height = 25
    width = 130
    # 创建画布
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象　
    draw = ImageDraw.Draw(im)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    x = 1
    for i in code_list:
        draw.text((16*x, 2), i, font=font, fill=fontcolor)
        x+=1
    del draw
    request.session['verifycode'] = verification_code

    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')