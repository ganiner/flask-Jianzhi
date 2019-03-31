# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com


from application import  app,db
from flask import Blueprint,render_template


adminIndexRoute=Blueprint( 'adminIndexRoute',__name__ )


@adminIndexRoute.route('/')
def index():
    return render_template("wait/index.html")

