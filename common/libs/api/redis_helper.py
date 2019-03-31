# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-10
#@Email : agamgn@163.com

import time
import asyncio

# 定义异步函数
from application import rdb, db
from common.models.jianzhikeer2 import JzkPost


async def redis_save_time(id):
    asyncio.sleep(11)
    if rdb.get(id) == None:
        jzkpost = db.session.query(JzkPost).filter_by(id=id).first()
        jzkpost.is_check = 1
        db.session.commit()
        print("存储成功")



