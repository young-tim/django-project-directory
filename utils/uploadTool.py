from django_demo.settings import FILE_URL, FILE_ROOT
from django_demo.exts import logger
import os
import uuid
from datetime import datetime


def upload_directory_path(filename):
    """重命名上传的文件名
    :param filename: 原文件名
    """
    # 获取文件后缀
    ext = filename.split('.')[-1]
    # 重命名文件名
    filename = '{}.{}'.format(uuid.uuid4().hex[:20], ext)
    # 绝对路径目录
    full_path = datetime.now().strftime(str(FILE_ROOT))
    # 相对路径目录
    path = datetime.now().strftime(str(FILE_URL))
    return full_path, path, filename


def uploadFile(file):
    """
    上传文件
    :param file: 文件流
    :return:
    """
    full_path, path, file_name =upload_directory_path(file.name)
    # 绝对路径文件
    full_file_path = os.path.join(full_path, file_name)
    # 相对路径文件
    file_path = os.path.join(path, file_name)

    # 自动创建目录
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    try:
        with open(full_file_path, 'wb') as fi:
            for i in file.chunks():
                fi.write(i)
    except Exception as e:
        logger.error(e)
        return file_name, "", -1, str(e)
    return file_name, file_path, 200, "OK"