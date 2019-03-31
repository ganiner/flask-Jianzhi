# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com


from application import app
from flask import request, g,session,redirect
import re
from common.libs.user.UserService import UserService
from common.models.jianzhikeer2 import JzkUser
from common.libs.UrlManager import UrlManager

@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    api_ignore_urls=app.config['API_IGNORE_URLS']
    app_ignore_urls=app.config['APP_IGNORE_URLS']
    img_ignore_urls=app.config['IMG_IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    user_info = check_login()

    g.current_user = None
    if user_info:
        g.current_user = user_info
        session['uid']=user_info.uid


    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return

    pattern = re.compile('%s' % "|".join(api_ignore_urls))
    if pattern.match(path):
        return

    pattern = re.compile('%s' % "|".join(app_ignore_urls))
    if pattern.match(path):
        return

    pattern = re.compile('%s' % "|".join(img_ignore_urls))
    if pattern.match(path):
        return

    if not user_info :
        return redirect( UrlManager.buildUrl( "/login/" ) )

    return





"""
判断用户是否已经登陆
"""

def check_login():
    cookies=request.cookies
    auth_cookie=cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else ""
    app.logger.info(auth_cookie)

    if auth_cookie is None:
        return False

    auth_info=auth_cookie.split("#")
    if len(auth_info) !=2:
        return False

    try:
        user_info=JzkUser.query.filter_by(uid=auth_info[1]).first()

    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] !=UserService.geneAuthCode(user_info):
        return False

    return user_info
