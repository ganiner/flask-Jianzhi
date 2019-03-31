# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

import json

from flask import Blueprint, g, Response

from application import app
from common.libs.Helper import ops_render

# 兼职models
from common.models.jianzhikeer2 import JzkUser
from common.models.jianzhikeer2 import JzkPost




jianzhiRoute=Blueprint("jianzhiRoute",__name__)

@jianzhiRoute.route("/")
def index():
    return ops_render("admin/jianzhi/jianzhi_home.html")


# 兼职管理
@jianzhiRoute.route("/jzmanagement/")
def jzmanagement():
    return ops_render('admin/jianzhi/jianzhi.html')


# 求职管理
@jianzhiRoute.route("/application/")
def application():
    return ops_render("admin/jianzhi/jianzhi_qiuzhi.html")



# 商家管理
@jianzhiRoute.route("/merchants/")
def merchants():
    return ops_render("admin/jianzhi/jianzhi_shangjia.html")





# 通知管理
@jianzhiRoute.route("/message/")
def message():
    return ops_render("admin/jianzhi/jianzhi_tongzhi.html")

# 添加通告
@jianzhiRoute.route("/add_messages/")
def add_messages():
    return ops_render("admin/jianzhi/add_messages.html")

# 添加广告
@jianzhiRoute.route("/add_ad/")
def add_ad():
    return ops_render("admin/jianzhi/add_ad.html")



# 账号管理

# 账号管理--我的账号
@jianzhiRoute.route("/mymesage/")
def mymessage():
    return ops_render("admin/jianzhi/jianzhi_message.html")

# 账号管理--管理员管理
@jianzhiRoute.route("/admin_list/")
def admin_list():
    user_list={}
    user_info=JzkUser.query.all()

    from application import app
    app.logger.debug(user_info[0].account)
    app.logger.debug(g.current_user)

    user_list['user_info']=user_info
    # app.logger.debug(g.user_info)
    app.logger.debug(user_list)
    app.logger.debug(user_list['user_info'])

    return ops_render("admin/jianzhi/jianzhi_guanliyuan.html",user_list)

# 账号管理---用户列表
@jianzhiRoute.route("/user_list/")
def user_list():
    user_list={}
    user_info=JzkUser.query.all()

    from application import app
    app.logger.debug(user_info[0].account)
    app.logger.debug(g.current_user)

    user_list['user_info']=user_info

    app.logger.debug(user_list)
    app.logger.debug(user_list['user_info'])

    return ops_render("admin/jianzhi/jianzhi_user_list.html",user_list)


# 账号管理---用户组管理
@jianzhiRoute.route("/groups/")
def groups():
    user_list={}
    user_info=JzkUser.query.all()

    from application import app
    app.logger.debug(user_info[0].account)
    app.logger.debug(g.current_user)

    user_list['user_info']=user_info
    app.logger.debug(g.user_info)
    app.logger.debug(user_list)
    app.logger.debug(user_list['user_info'])
    return ops_render("admin/jianzhi/jianzhi_groups.html",user_list)







# 统计管理
# 统计管理--日统计
@jianzhiRoute.route("/statisticsday/")
def statisticsday():
    return ops_render("admin/jianzhi/jianzhi_tongjiday.html")


# 统计管理--月统计
@jianzhiRoute.route("/statisticsmouth/")
def statisticsmouth():
    return ops_render("admin/jianzhi/jianzhi_tongjiday.html")


# 系统管理

# 系统管理--系统设置
@jianzhiRoute.route("/system/")
def system():
    pass
    # return ops_render("admin/jianzhi/jianzhi_tongjiday.html")

# 系统管理--日志管理
@jianzhiRoute.route("/log/")
def log():
    pass


# 系统管理--系统信息
@jianzhiRoute.route("/systeminfo/")
def systeminfo():
    return ops_render("admin/jianzhi/te.html")


@jianzhiRoute.route("/te/")
def te():
    lists=[]
    tric={}
    query = JzkPost.query
    a=query.order_by(JzkPost.id.desc()).all()
    for i in a:
        tric["title"]=i.title
        tric["contents"]=i.contents
        lists.append(tric)
    ga={}
    ga['code']=0
    ga['msg']=''
    ga['count']=1000
    ga['data']=lists
    return Response(json.dumps(ga))




