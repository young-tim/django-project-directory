# -*- coding: utf-8 -*-
# @Time : 2021/9/5 1:39 上午
# @Author : Tim
# @Email : 1163154905@qq.com
# @PythonVersion : Python 3

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views import View


# Create your views here.

# @require_http_methods(["GET", "POST"])
# def indexView(request):
#     context = {
#         "code": 200,
#         "msg": "OK",
#         "data": None,
#     }
#     return JsonResponse(context)
#     # return render(request, 'index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        print(request)
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        print(request)
        context = {
            "code": 200,
            "msg": "OK",
            "data": None,
        }
        return JsonResponse(context)
