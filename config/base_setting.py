# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com


SERVER_PORT=5000
SQLALCHEMY_ECHO = True
# mysql配置

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:916149@127.0.0.1:3306/jianzhikeer2?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False


RELEASE_VERSION='20190101120000'
AUTH_COOKIE_NAME='jianzhikeer'
SECRET_KEY='abcsdfdsfsdgdfsgdfsgfsgfsggfdhbgf'


# 分页
PAGE_SIZE = 1
PAGE_DISPLAY = 5

##过滤url,在过滤器中配置，现在先把api的
IGNORE_URLS = [
    "^/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]
APP_IGNORE_URLS=[
    "^/app"
]
IMG_IGNORE_URLS=[
    "^/attachement"
]







