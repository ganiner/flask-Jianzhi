# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

import json
from io import BytesIO

from flask import Blueprint, request, make_response, redirect, session
from flask.json import jsonify

from application import app
from common.libs.Helper import ops_render
from common.libs.UrlManager import UrlManager
from common.libs.auth_code import get_verify_code
from common.models.jianzhikeer2 import JzkUser
from common.libs.user.UserService import UserService


adminUserRoute=Blueprint("adminUserRoute",__name__)


@adminUserRoute.route("/",methods=['GET','POST'])
def login():
    """管理人员登陆"""



    if request.method == "GET":
        return ops_render("admin/login.html")

    resp = {'code': 200, 'msg': '登录成功~~', 'data': {}}
    req = request.values
    login_name = req["username"] if 'username' in req else ''
    login_pwd = req['password'] if 'password' in req else ''
    login_codes=req['codes'] if "codes" in req else ""
    app.logger.debug('*'*100)
    app.logger.debug(resp)
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名或密码"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名或密码"
        return jsonify(resp)

    if login_codes.lower()!=session['code'] or len(login_codes)<1:
        resp['code']=-1
        resp['msg']="请输入正确的验证码"
        return jsonify(resp)


    user_info = JzkUser.query.filter_by(account=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码-1~~"
        return jsonify(resp)

    if not UserService.genePwd(user_info.password, login_pwd):
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码-2~~"
        return jsonify(resp)

    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24)  # 保存1天
    return response



@adminUserRoute.route("/logout/")
def logout():
    """管理人员退出"""
    response=make_response(redirect(UrlManager.buildUrl("/login/")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response



# 验证码路由
@adminUserRoute.route('/code/')
def code():
    """生成验证码图片流"""
    image, code = get_verify_code()
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['code'] = code.lower()
    return response


