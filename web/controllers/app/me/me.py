# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-11
#@Email : agamgn@163.com




from flask import Blueprint

from common.libs.Helper import ops_render
from web.interceptors.getwx import admin_login_req

appMe=Blueprint("appMe",__name__)



@admin_login_req
@appMe.route("/")
def index():
    return ops_render("app/me.html")



@admin_login_req
@appMe.route("/jianzhi_list/")
def jianzhi_list():
    return ops_render("app/jianzhi_list.html")


@admin_login_req
@appMe.route("/collection/")
def collection():
    return ops_render("app/collection.html")



@admin_login_req
@appMe.route("/post_list/")
def post_list():
    return ops_render("app/post_list.html")


@admin_login_req
@appMe.route("/feedback/")
def feedback():
    return ops_render("app/feedback.html")



@admin_login_req
@appMe.route("/modifying_data/")
def modifying_data():
    return ops_render("app/modifying_data.html")


@admin_login_req
@appMe.route("/add_sj/")
def add_sj():
    return ops_render("app/add_shangjia.html")



@admin_login_req
@appMe.route("/te/")
def te():
    return ops_render("app/add_shangjia.html")
