# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

import hashlib

from werkzeug.security import check_password_hash, generate_password_hash


class UserService:


    @staticmethod
    def geneAuthCode(user_info = None ):
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.uid, user_info.account, user_info.password, user_info.sex)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    # 密码解密机制
    @staticmethod
    def genePwd(salt,pwd):
       return check_password_hash(salt,pwd)

    # 密码加密机制
    @staticmethod
    def jiaPwd(pwd):
        return generate_password_hash(pwd)