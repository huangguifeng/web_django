from django.shortcuts import render

# Create your views here.

def register(request):

    title = '天天生鲜-注册'
    context = {"title":title}
    return render(request,'df_user/register.html',context)



def login(request):
    title = '天天生鲜-登录'
    context = {"title":title}
    return render(request,'df_user/login.html',context)

