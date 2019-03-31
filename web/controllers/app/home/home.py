# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-11
#@Email : agamgn@163.com




from flask import Blueprint, session

from common.libs.Helper import ops_render
from web.interceptors.getwx import admin_login_req

appHome=Blueprint("appHome",__name__)



@admin_login_req
@appHome.route("/")
def index():
    return ops_render("app/index.html")


@admin_login_req
@appHome.route("/add/")
def add():
    return ops_render("app/add_shangjia.html")



@admin_login_req
@appHome.route("/detal/")
def detal():
    return ops_render("app/detal.html")

