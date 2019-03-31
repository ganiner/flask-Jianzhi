# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-11
#@Email : agamgn@163.com



from flask import Blueprint
from web.interceptors.getwx import admin_login_req
from common.libs.Helper import ops_render

appPosts=Blueprint("appPosts",__name__)


@admin_login_req
@appPosts.route("/")
def index():
    return ops_render("app/post.html")