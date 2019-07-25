#!/usr/bin/python
# -*- coding: utf-8 -*
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

currentuser = '请登录'


# 第二种方式
class Usermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global currentuser
        currentuser = request.session.get('username', '请登录')

        response = self.get_response(request)

        return response


def mycontext(request):
    return {'currentuser': currentuser}


