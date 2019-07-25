from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from django.views import View
from .models import BlogUser
import datetime


def index(request):
    return HttpResponse('user_index')


class UserRegister(View):
    def get(self, request):
        return render(request, 'user/user_register.html')

    def post(self, request):
        message = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeatpassword = request.POST.get('repeatpassword')
        email = request.POST.get('email')
        if password == repeatpassword:
            # 验证用户是否已经存在
            if BlogUser.objects.filter(username=username).first():
                message = '该用户名已经被注册'
                return render(request, 'user/user_register.html', context={'message': message})
            else:
                user = BlogUser()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                return redirect(reverse('user_login'))
        else:
            message = '两次密码输入不相同'
            return render(request, 'user/user_register.html', context={'message': message})


class UserLogin(View):
    def get(self, request):
        return render(request, 'user/user_login.html')

    def post(self, request):
        message = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证账号密码
        if BlogUser.objects.filter(username=username, password=password).first():
            # 设置session cookie
            request.session['username'] = username
            # 设置30天后过期
            request.session.set_expiry(datetime.timedelta(days=30))
            return redirect(reverse('bloglist'))
        else:
            message = '账号或密码错误'
            return render(request, 'user/user_login.html', context={'message': message})


class UserUpdatePassword(View):
    def get(self, request):
        return render(request, 'user/user_updatepassword.html')

    def post(self, request):
        message = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        newpassword = request.POST.get('newpassword')
        user = BlogUser.objects.filter(username=username, password=password).first()
        if user:
            if password == newpassword:
                message = '新密码不能和原密码相同'
                return render(request, 'user/user_updatepassword.html', context={'message': message})
            else:
                user.password = newpassword
                user.save()
                return redirect(reverse('user_login'))
        else:
            message = '账号或密码错误'
            return render(request, 'user/user_updatepassword.html', context={'message': message})


def user_logout(request):
    # 删除当前的会话数据并删除会话的Cookie
    request.session.flush()
    return redirect(reverse('user_login'))

