from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from django.views import View
from .models import BlogUser
import datetime

# 导入auth的登录、登出、验证等方法
from django.contrib.auth import login, logout, authenticate
# 导入相关模型
from django.contrib.auth.models import User ,Permission, Group


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
            # if BlogUser.objects.filter(username=username).first():
            # auth中的User
            if User.objects.filter(username=username).first():
                message = '该用户名已经被注册'
                return render(request, 'user/user_register.html', context={'message': message})
            else:
                # auth中的User
                User.objects.create_user(username=username, password=password, email=email)
                # user = BlogUser()
                # user.username = username
                # user.password = password
                # user.email = email
                # user.save()
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
        next_url = request.GET.get('next')
        # 验证账号密码
        # if BlogUser.objects.filter(username=username, password=password).first():
        # auth中的User
        user = authenticate(username=username, password=password)
        if user:
            # auth Login
            login(request, user)
            # # 设置session cookie
            # request.session['username'] = username
            # # 设置30天后过期
            # request.session.set_expiry(datetime.timedelta(days=30))
            if next_url:
                return redirect(next_url)
            else:
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
        # user = BlogUser.objects.filter(username=username, password=password).first()
        # 验证账号密码
        user = authenticate(username=username, password=password)
        if user:
            if password == newpassword:
                message = '新密码不能和原密码相同'
                return render(request, 'user/user_updatepassword.html', context={'message': message})
            else:
                # auth_user 修改密码
                user.set_password(newpassword)
                user.save()
                # u = User.objects.filter(username=username).first()
                # u.check_password(newpassword)
                # print(u, '*************')
                # u.password = newpassword
                # u.save()
                # user.password = newpassword
                # user.save()
                return redirect(reverse('user_login'))
        else:
            message = '账号或密码错误'
            return render(request, 'user/user_updatepassword.html', context={'message': message})


def user_logout(request):
    # 删除当前的会话数据并删除会话的Cookie
    # request.session.flush()
    logout(request)
    return redirect(reverse('user_login'))

