from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from django.views import View

def index(request):
    return HttpResponse('user_index')


class UserRegister(View):
    def get(self, request):
        return render(request, 'user/user_register.html')

    def post(self,request):
        return render(request, 'user/user_register.html')


class UserLogin(View):
    def get(self, request):
        return render(request, 'user/user_login.html')

    def post(self, request):
        return render(request, 'user/user_login.html')


class UserUpdatePassword(View):
    def get(self, request):
        return render(request, 'user/user_updatepassword.html')

    def post(self, request):
        return render(request, 'user/user_updatepassword.html')


def user_logout(request):
    return redirect(reverse('user_index'))

