import datetime
import os


def random_name():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def file_extension(path):
    return os.path.splitext(path)[1]


def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


def create(filepath):
    msg = "用户名存在"
    if not os.path.exists(filepath):
        os.makedirs(filepath)
        msg = "成功创建"
        return msg
    else:
        return msg
