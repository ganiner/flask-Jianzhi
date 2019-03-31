# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com


from flask import session
from application import db


class getwechat:
    def __init__(self,appid,redirect_uri):
        self.code=''
        self.access_token=''
        self.appid=appid
        self.redirect_uri=redirect_uri

    def getcode(self):
        url='https://open.weixin.qq.com/connect/oauth2/' \
            'authorize?appid={0}&redirect_uri={1}&response_type=code&' \
            'scope=snsapi_userinfo&state=STATE#wechat_redirect'.format(self.appid,self.redirect_uri)

    def gettoken_openid(self):
        pass

    def msg(self):
        pass

    def save(self):
        pass