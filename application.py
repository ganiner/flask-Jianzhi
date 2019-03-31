# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

import os
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_restful import Api

class AppLication(Flask):
    """根据配置按需加载，抽象出配置类"""

    def __init__(self,import_name,template_folder=None,root_path=None):
        super(AppLication,self).__init__(import_name,template_folder=template_folder,static_folder=None,root_path=root_path)
        self.config.from_pyfile("config\\base_setting.py")
        db.init_app(self)



db=SQLAlchemy()
rdb=redis.Redis()
app=AppLication(__name__,template_folder=os.getcwd()+"\\web\\templates\\",root_path=os.getcwd())
api=Api(app)
manager=Manager(app)
"""
函数模板
"""

from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')

