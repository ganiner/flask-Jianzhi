# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com


from application import app
from flask import session
from functools import wraps
from common.models.jianzhikeer2 import JzkWxUser



def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if 'uid' not in session:
            getwxs()
        return f(*args,**kwargs)
    return decorated_function


@app.before_request
def getwxs():
    if 'uid' not in session:
        # 调用微信

        session['uid']='1'


