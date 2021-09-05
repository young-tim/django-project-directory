# -*- coding: utf-8 -*-
# @Time : 2021/9/5 2:31 上午
# @Author : Tim
# @Email : 1163154905@qq.com
# @PythonVersion : Python 3
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from utils.uploadTool import uploadFile


@require_http_methods(["POST"])
def uploadMediaView(request):
    if "upload_file" not in request.FILES:
        context = {
            "code": -1,
            "msg": "参数缺失: <upload_file>",
            "data": None,
        }
        return JsonResponse(context)

    file = request.FILES["upload_file"]
    file_name, file_path, code, msg = uploadFile(file)
    context = {
        "code": code,
        "msg": msg,
        "data": {
            "file_name": file_name,
            "file_path": file_path,
        }
    }
    return JsonResponse(context)