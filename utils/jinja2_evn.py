# -*- coding: utf-8 -*-
# @Time : 2021/8/8 11:46 下午
# @Author : Tim
# @Email : 1163154905@qq.com
# @PythonVersion : Python 3
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_env(**opts):
    env = Environment(**opts)
    env.globals.update({
        "static": staticfiles_storage.url,  # 获取静态文件前缀
        "url": reverse  # 反向解析
    })
    return env