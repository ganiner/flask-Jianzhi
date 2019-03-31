# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

from flask import Blueprint,render_template

from common.libs.Helper import ops_render

MainRoute=Blueprint("MainRoute",__name__)


@MainRoute.route("/")
def index():
    return ops_render("admin/index.html")


