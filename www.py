# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

from application import app
import web.controllers.api.api_v1


"""
统一拦截器
"""
from web.interceptors.getwx import *

from web.interceptors.Authinterceptor import *



'''
蓝图功能，对所有的url进行蓝图功能配置
'''
from web.controllers.admin.index import adminIndexRoute
from web.controllers.admin.user.User import adminUserRoute
from web.controllers.static import route_static
from web.controllers.admin.main.Mains import MainRoute
from web.controllers.admin.jianzhi.jianzhi import jianzhiRoute


app.register_blueprint(adminIndexRoute,url_prefix="/")
app.register_blueprint(adminUserRoute,url_prefix="/login")
app.register_blueprint(MainRoute,url_prefix="/main")
app.register_blueprint(jianzhiRoute,url_prefix="/jianzhi")




app.register_blueprint(route_static,url_prefix='/static')




# 微站蓝图
from web.controllers.app.home.home import appHome
from web.controllers.app.posts.posts import appPosts
from web.controllers.app.me.me import appMe

app.register_blueprint(appHome,url_prefix='/app/apphome')
app.register_blueprint(appMe,url_prefix='/app/appme')
app.register_blueprint(appPosts,url_prefix='/app/apposts')







