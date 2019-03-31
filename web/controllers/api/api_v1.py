# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

import datetime

from flask import jsonify, session, make_response
from sqlalchemy import func

from application import api, db,rdb
from flask_restful import Resource,request,reqparse

from common.libs.api.redis_helper import redis_save_time
from common.models.jianzhikeer2 import JzkUser, JzkUserGroup, JzkPost, JzkSignUp, JzkIsMerchant, JzkInform, \
    JzkAdvertising, JzkCollect


# 用户信息相关

class userMessage(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('page', type=str)
        self.parser.add_argument('limit', type=str)

    def get(self):
        data = self.parser.parse_args()
        page = int(data.get('page'))
        limit = int(data.get('limit'))
        pages = (page - 1) * limit
        limits = page * limit
        user_infos = JzkUser.query.all()[pages:limits]
        users=[]
        user={}
        for user_info in user_infos:
            user['account']=user_info.account
            user['nickname']=user_info.nickname
            user['sex'] = user_info.sex
            user['avator']=user_info.avator
            user['groud']=user_info.groud
            user['mail']=user_info.mail
            user['tel']=user_info.tel
            user['name']=user_info.name
            user['credit'] = user_info.credit
            user['birthday']=user_info.birthday
            user['address']=user_info.address
            user['qqnum']=user_info.qqnum
            user['payzhifubao']=user_info.payzhifubao
            user['education']=user_info.education
            user['experience']=user_info.experience
            user['freetime']=user_info.freetime
            user['province']=user_info.province
            user['city'] = user_info.city
            user['country'] = user_info.country

            users.append(user)
            user={}
        res = {'code': 0, 'msg': "获取成功", 'count': JzkUser.query.count(), 'data': users}
        return jsonify(res)


    def post(self):
        resp={'code':200,'msg':'修改成功'}
        dict = request.form
        return jsonify(resp)


# 用户组
class userGroup(Resource):
    def get(self):
        group_infos = JzkUserGroup.query.all()
        groups=[]
        group={}
        for group_info in group_infos:
            group['name']=group_info.name
            groups.append(group)
            group={}
        return groups

    def post(self):
        pass

#兼职信息相关
class part_time(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('is_check', type=int)
        self.parser.add_argument('page', type=str)
        self.parser.add_argument('limit', type=str)
    # 获取信息
    def get(self):
        data = self.parser.parse_args()
        page=int(data.get('page'))
        limit=int(data.get('limit'))
        pages=(page-1)*limit
        limits=page*limit
        is_check=data.get("is_check")
        jianzhis = []
        jianzhi = {}
        if is_check==1:
            jianzhi_infos =JzkPost.query.filter_by(is_check=1).all()[pages:limits]
            for jianzhi_info in jianzhi_infos:
                jianzhi['id'] = jianzhi_info.id
                jianzhi['uid'] = jianzhi_info.uid
                jianzhi['title'] = jianzhi_info.title
                jianzhi['wages'] = jianzhi_info.wages
                jianzhi['benefits'] = jianzhi_info.benefits
                jianzhi['contents'] = jianzhi_info.content
                jianzhi['people'] = jianzhi_info.people
                jianzhi['people_tel'] = jianzhi_info.people_tel
                jianzhi['need_num'] = jianzhi_info.need_num
                jianzhi['jianzhi_type'] = jianzhi_info.jianzhi_type
                jianzhi['start_time'] = jianzhi_info.start_time
                jianzhi['end_time'] = jianzhi_info.end_time
                jianzhi['addres'] = jianzhi_info.addres
                jianzhi['jianzhi_time_type'] = jianzhi_info.jianzhi_time_type
                jianzhi['other'] = jianzhi_info.other
                jianzhi['is_top'] = jianzhi_info.is_top
                jianzhis.append(jianzhi)
                jianzhi = {}

            res = {'code': 0, 'msg': "获取成功", 'count': JzkPost.query.filter_by(is_check=1).count(), 'data': jianzhis}
            return jsonify(res)
        # 未审核
        if is_check==0:
            jianzhi_infos = JzkPost.query.filter_by(is_check=0).all()[pages:limits]
            for jianzhi_info in jianzhi_infos:
                jianzhi['id'] = jianzhi_info.id
                jianzhi['uid'] = jianzhi_info.uid
                jianzhi['title'] = jianzhi_info.title
                jianzhi['wages'] = jianzhi_info.wages
                jianzhi['benefits'] = jianzhi_info.benefits
                jianzhi['contents'] = jianzhi_info.content
                jianzhi['people'] = jianzhi_info.people
                jianzhi['people_tel'] = jianzhi_info.people_tel
                jianzhi['need_num'] = jianzhi_info.need_num
                jianzhi['jianzhi_type'] = jianzhi_info.jianzhi_type
                jianzhi['start_time'] = jianzhi_info.start_time
                jianzhi['end_time'] = jianzhi_info.end_time
                jianzhi['addres'] = jianzhi_info.addres
                jianzhi['jianzhi_time_type'] = jianzhi_info.jianzhi_time_type
                jianzhi['other'] = jianzhi_info.other
                jianzhi['is_top'] = jianzhi_info.is_top
                jianzhis.append(jianzhi)
                jianzhi = {}

            res = {'code': 0, 'msg': "获取成功", 'count': JzkPost.query.filter_by(is_check=0).count(), 'data': jianzhis}
            return jsonify(res)




    def post(self):
        reqs={'code':200,'msg':'发表成功','data':{}}
        dict = request.form
        uid=session['uid']
        jzposts = JzkPost(
            uid=uid,
            title=dict['title'],
            content=dict['content'],
            wages=dict['wages'],
            benefits=dict['benefits'],
            need_num=dict['need_num'],
            start_time=dict['start_time'],
            end_time=dict['end_time'],
            addres=dict['addres'],
            other=dict['other'],
            jianzhi_type=dict['jianzhi_type'],
            jianzhi_time_type=dict['jianzhi_time_type'],
            people=dict['people'],
            people_tel=dict['people_tel'],
        )

        db.session.add(jzposts)
        db.session.commit()
        return jsonify(reqs)

    def put(self):
        reqs = {'code': 200, 'msg': '审核成功', 'data': {}}
        pid = request.form
        jzkpost=JzkPost.query.filter_by(id=pid['id']).first()
        jzkpost.is_check=1
        db.session.commit()
        return jsonify(reqs)

    def delete(self):
        reqs = {'code': 200, 'msg': '删除成功', 'data': {}}
        pid = request.form
        jzkpost = JzkPost.query.filter_by(id=pid).first()
        db.session.delete(jzkpost)
        db.session.commit()
        return jsonify(reqs)



# 求职相关
class sign_up(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('is_baoming', type=int)
        self.parser.add_argument('is_confirme', type=int)
        self.parser.add_argument('is_sign_in', type=int)
        self.parser.add_argument('is_complete', type=int)
        self.parser.add_argument('page', type=str)
        self.parser.add_argument('limit', type=str)

    def get(self):

        data = self.parser.parse_args()
        page = int(data.get('page'))
        limit = int(data.get('limit'))
        is_baoming=data.get("is_baoming")
        is_confirme = data.get("is_confirme")
        is_sign_in = data.get("is_sign_in")
        is_complete = data.get("is_complete")
        pages = (page - 1) * limit
        limits = page * limit

        # 已签到
        if is_sign_in==1:
            sign_ups = []
            sign_up = {}
            sign_up_infos = JzkSignUp.query.filter_by(is_sign_in=1).all()[pages:limits]
            for sign_up_info in sign_up_infos:
                sign_up['uid'] = sign_up_info.uid
                # 在这里可以查询
                sign_up['pid'] = sign_up_info.pid

                sign_ups.append(sign_up)
                sign_up = {}

            res = {'code': 0, 'msg': "获取成功", 'count': JzkSignUp.query.filter_by(is_sign_in=1).count(), 'data': sign_ups}
            return jsonify(res)
        # 已录用
        if is_confirme==1:
            sign_ups = []
            sign_up = {}
            sign_up_infos = JzkSignUp.query.filter_by(is_confirme=1).all()[pages:limits]
            for sign_up_info in sign_up_infos:
                sign_up['uid'] = sign_up_info.uid
                sign_up['pid'] = sign_up_info.pid

                sign_ups.append(sign_up)
                sign_up = {}

            res = {'code': 0, 'msg': "获取成功", 'count': JzkSignUp.query.filter_by(is_confirme=1).count(), 'data': sign_ups}
            return jsonify(res)
        # 已报名
        if is_baoming==1:
            sign_ups = []
            sign_up = {}
            sign_up_infos = JzkSignUp.query.all()[pages:limits]
            for sign_up_info in sign_up_infos:
                sign_up['uid'] = sign_up_info.uid
                sign_up['pid'] = sign_up_info.pid


                sign_ups.append(sign_up)
                sign_up = {}

            res = {'code': 0, 'msg': "获取成功", 'count': JzkSignUp.query.count(),
                   'data': sign_ups}
            return jsonify(res)
        # 已完成
        if is_complete:
            sign_ups = []
            sign_up = {}
            sign_up_infos = JzkSignUp.query.filter_by(is_complete=1).all()[pages:limits]
            for sign_up_info in sign_up_infos:
                sign_up['uid'] = sign_up_info.uid
                sign_up['pid'] = sign_up_info.pid

                sign_ups.append(sign_up)
                sign_up = {}

            res = {'code': 0, 'msg': "获取成功", 'count': JzkSignUp.query.filter_by(is_complete=1).count(),
                   'data': sign_ups}
            return jsonify(res)



# 商家相关
class business(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('is_check', type=int)
        self.parser.add_argument('is_vip', type=int)
        self.parser.add_argument('page', type=str)
        self.parser.add_argument('limit', type=str)

    def get(self):
        data = self.parser.parse_args()
        page = int(data.get('page'))
        limit = int(data.get('limit'))
        pages = (page - 1) * limit
        limits = page * limit
        is_check = data.get("is_check")

        is_vip = data.get("is_vip")
        jianzhis = []
        jianzhi = {}
        # 未审核
        if is_check==0:
            jzkismerchant_infos = JzkIsMerchant.query.filter_by(is_check=0).all()[pages:limits]
            for jianzhi_info in jzkismerchant_infos:
                jianzhi['id'] = jianzhi_info.id
                jianzhi['uid'] = jianzhi_info.uid
                jianzhi['name'] = jianzhi_info.name
                jianzhi['address'] = jianzhi_info.address
                jianzhi['detail'] = jianzhi_info.detail
                jianzhi['people_name'] = jianzhi_info.people_name
                jianzhi['people_tel'] = jianzhi_info.people_tel
                jianzhi['lincese'] = jianzhi_info.lincese
                jianzhi['grade'] = jianzhi_info.grade
                jianzhi['is_vip'] = jianzhi_info.is_vip
                jianzhis.append(jianzhi)
                jianzhi = {}
            res = {'code': 0, 'msg': "获取成功", 'count': JzkIsMerchant.query.filter_by(is_check=0).count(), 'data': jianzhis}
            return jsonify(res)
        # 已入住
        if is_check==1:
            jzkismerchant_infos = JzkIsMerchant.query.filter_by(is_check=1).all()[pages:limits]
            for jianzhi_info in jzkismerchant_infos:
                jianzhi['id'] = jianzhi_info.id
                jianzhi['uid'] = jianzhi_info.uid
                jianzhi['name'] = jianzhi_info.name
                jianzhi['address'] = jianzhi_info.address
                jianzhi['detail'] = jianzhi_info.detail
                jianzhi['people_name'] = jianzhi_info.people_name
                jianzhi['people_tel'] = jianzhi_info.people_tel
                jianzhi['lincese'] = jianzhi_info.lincese
                jianzhi['grade'] = jianzhi_info.grade
                jianzhi['is_vip'] = jianzhi_info.is_vip
                jianzhis.append(jianzhi)
                jianzhi = {}
            res = {'code': 0, 'msg': "获取成功", 'count': JzkIsMerchant.query.filter_by(is_check=1).count(), 'data': jianzhis}
            return jsonify(res)
        # 是vip
        if is_check is None and is_vip==1:

            jzkismerchant_infos = JzkIsMerchant.query.filter_by(is_vip=1).all()[pages:limits]
            for jianzhi_info in jzkismerchant_infos:
                jianzhi['id'] = jianzhi_info.id
                jianzhi['uid'] = jianzhi_info.uid
                jianzhi['name'] = jianzhi_info.name
                jianzhi['address'] = jianzhi_info.address
                jianzhi['detail'] = jianzhi_info.detail
                jianzhi['people_name'] = jianzhi_info.people_name
                jianzhi['people_tel'] = jianzhi_info.people_tel
                jianzhi['lincese'] = jianzhi_info.lincese
                jianzhi['grade'] = jianzhi_info.grade
                jianzhi['is_vip'] = jianzhi_info.is_vip
                jianzhis.append(jianzhi)
                jianzhi = {}
            res = {'code': 0, 'msg': "获取成功", 'count': JzkIsMerchant.query.filter_by(is_vip=1).count(), 'data': jianzhis}
            return jsonify(res)

    # 商家注册s
    def post(self):
        reqs = {'code': 200, 'msg': '申请成功，请等待审核', 'data': {}}
        dict = request.form
        uid = session['uid']
        jzkismerchant = JzkIsMerchant(
            uid=uid,
            name=dict['jz_shop_name'],
            address=dict['jz_shop_address'],
            detail=dict['jz_shop_detal'],
            people_name=dict['jz_shop_people'],
            people_tel=dict['jz_shop_tel'],
            lincese=dict['jz_shop_lincese'],
        )

        db.session.add(jzkismerchant)
        db.session.commit()
        return jsonify(reqs)



# 公告相关
class inform(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('page', type=str)
        self.parser.add_argument('limit', type=str)

    def get(self):
        informs=[]
        informa={}
        data = self.parser.parse_args()
        page = int(data.get('page'))
        limit = int(data.get('limit'))
        pages = (page - 1) * limit
        limits = page * limit
        inform_infos = JzkInform.query.order_by(JzkInform.id.desc())[pages:limits]
        for group_info in inform_infos:
            informa['id'] = group_info.id
            informa['content']=group_info.content
            informa['time'] = group_info.time
            informs.append(informa)
            informa={}
        res = {'code': 0, 'msg': "获取成功", 'count': JzkInform.query.count(), 'data': informs}
        return jsonify(res)


    def post(self):

        reqs = {'code': 200, 'msg': '发表成功', 'data': {}}
        dict = request.form
        # 后台还要写逻辑判断的哦
        jzkinform = JzkInform(
            content=dict['content'],
        )
        db.session.add(jzkinform)
        db.session.commit()
        return jsonify(reqs)




# 广告相关
class advertising(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('page', type=str)
        self.parser.add_argument('limit', type=str)

    def get(self):
        jzkadvertisings=[]
        jzkadvertising={}
        data = self.parser.parse_args()
        page = int(data.get('page'))
        limit = int(data.get('limit'))
        pages = (page - 1) * limit
        limits = page * limit
        jzkadvertising_infos = JzkAdvertising.query.all()[pages:limits]
        for jzkadvertising_info in jzkadvertising_infos:
            jzkadvertising['id'] = jzkadvertising_info.id
            jzkadvertising['title']=jzkadvertising_info.title
            jzkadvertising['content'] = jzkadvertising_info.content
            jzkadvertising['link'] = jzkadvertising_info.link
            jzkadvertising['time'] = jzkadvertising_info.time
            jzkadvertisings.append(jzkadvertising)
            jzkadvertising={}
        res = {'code': 0, 'msg': "获取成功", 'count': JzkAdvertising.query.count(), 'data': jzkadvertisings}
        return jsonify(res)

    def post(self):
        reqs = {'code': 200, 'msg': '发表成功', 'data': {}}
        dict = request.form
        Jzkadvertising = JzkAdvertising(
            title=dict['title'],
            content=dict['content'],
            link=dict['link'],
        )
        db.session.add(Jzkadvertising)
        db.session.commit()
        return jsonify(reqs)

# 微站的发帖/修改到了上面的一个里面
class app_posts(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)


    def get(self):
        data = self.parser.parse_args()
        reqs = {'code': 100, 'msg': '没有注册成商家', 'data': {}}
        id = int(data.get('id'))
        user_infos = JzkUser.query.filter_by(uid=id).first()
        if user_infos.is_merchant==0:
            return jsonify(reqs)
        reqs['code']=200
        reqs['msg']="欢迎尊敬的商家"
        return jsonify(reqs)

    def post(self):
        reqs={'code':200,'msg':'发表成功','data':{}}
        dict = request.form
        uid=session['uid']

        if dict['is_zhiding'] =='true':
            istop=1

        else:
            istop=0
        jzposts = JzkPost(
            uid=uid,
            title=dict['title'],
            content=dict['content'],
            wages=dict['wages'],
            benefits=dict['benefits'],
            need_num=dict['need_num'],
            start_time=dict['start_time'],
            end_time=dict['end_time'],
            addres=dict['addres'],
            other=dict['other'],
            is_top=istop,
            jianzhi_type=dict['jianzhi_type'],
            jianzhi_time_type=dict['jianzhi_time_type'],
            people=dict['people'],
            people_tel=dict['people_tel'],
        )
        db.session.add(jzposts)
        db.session.commit()
        id=db.session.query(func.max(JzkPost.id)).one()[0]
        rdb.set(id, '倒计时的时间', 10)
        try:
            redis_save_time(id).send(None)
        except StopIteration as e:
            print("我已经停止了")

        return jsonify(reqs)


class app_me(Resource):
    def get(self):

        user_infos = JzkUser.query.all()
        users=[]
        user={}
        for user_info in user_infos:
            user['uid']=user_info.uid
            user['account']=user_info.account
            user['nickname']=user_info.nickname
            user['sex'] = user_info.sex
            user['avator']=user_info.avator
            user['groud']=user_info.groud
            user['mail']=user_info.mail
            user['tel']=user_info.tel
            user['name']=user_info.name
            user['credit'] = user_info.credit
            user['birthday']=user_info.birthday
            user['address']=user_info.address
            user['qqnum']=user_info.qqnum
            user['payzhifubao']=user_info.payzhifubao
            user['education']=user_info.education
            user['experience']=user_info.experience
            user['freetime']=user_info.freetime
            user['province']=user_info.province
            user['city'] = user_info.city
            user['country'] = user_info.country

            users.append(user)
            user={}
        return users

    def post(self):
        user=JzkUser.query.filter_by(uid=2).first()
        db.session.delete(user)
        db.session.commit()

# 微站的帖子详情
class app_detal(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

        self.parser.add_argument('id', type=int)

    def get(self):
        data = self.parser.parse_args()
        ids = int(data.get('id'))
        jianzhi={}
        jianzhi_info = JzkPost.query.filter_by(id=ids).first()
        jianzhi['uid'] = jianzhi_info.uid
        jianzhi['title'] = jianzhi_info.title
        jianzhi['wages'] = jianzhi_info.wages
        jianzhi['benefits'] = jianzhi_info.benefits
        jianzhi['content'] = jianzhi_info.content
        jianzhi['people'] = jianzhi_info.people
        jianzhi['people_tel'] = jianzhi_info.people_tel
        jianzhi['need_num'] = jianzhi_info.need_num
        jianzhi['jianzhi_type'] = jianzhi_info.jianzhi_type
        jianzhi['start_time'] = jianzhi_info.start_time
        jianzhi['end_time'] = jianzhi_info.end_time
        jianzhi['addres'] = jianzhi_info.addres
        jianzhi['jianzhi_time_type'] = jianzhi_info.jianzhi_time_type
        jianzhi['other'] = jianzhi_info.other
        jianzhi['is_top'] = jianzhi_info.is_top
        jianzhi['times'] =str((datetime.datetime.now() - jianzhi_info.public_time).seconds)+"秒前"
        res = {'code': 200, 'msg': "获取成功", 'data': jianzhi}


        return jsonify(res)


# 微站的用户信息
class app_user_message(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
    def get(self):
        data = self.parser.parse_args()
        id = int(data.get('id'))

        signup={}
        signup['is_confirme']=0
        signup['is_sign_in']=0
        signup['is_complete']=0
        # 帖子的id
        pid=[]
        signup_infos=JzkSignUp.query.filter_by(uid=id).all()
        for signup_info in signup_infos:
            pid.append(JzkPost.query.filter_by(id=signup_info.pid).first().id)
            if signup_info.is_confirme ==1:
                signup['is_confirme']+=1
            if signup_info.is_sign_in==1:
                signup['is_sign_in']+=1
            if signup_info.is_complete==1:
                signup['is_complete']+=1
        #已录用
        on_confirme_count=signup['is_confirme']
        # 已签到
        on_sign_in_count = signup['is_sign_in']
        # 已完成
        on_complete_count = signup['is_complete']
        # 已报名
        on_sign_on_count = JzkSignUp.query.filter_by(uid=id).count()

        signupser = {"pids":pid,"on_sign_on_count":on_sign_on_count,"on_confirme_count":on_confirme_count,"on_sign_in_count":on_sign_in_count,"on_complete_count":on_complete_count}

        # 主要是用户信息
        user={}
        user_info = JzkUser.query.filter_by(uid=id).first()
        user['account']=user_info.account
        user['nickname']=user_info.nickname
        user['sex'] = user_info.sex
        user['avator']=user_info.avator
        user['group']=user_info.group
        user['mail']=user_info.mail
        user['tel']=user_info.tel
        user['name']=user_info.name
        user['credit'] = user_info.credit
        user['birthday']=user_info.birthday
        user['address']=user_info.address
        user['qqnum']=user_info.qqnum
        user['payzhifubao']=user_info.payzhifubao
        user['education']=user_info.education
        user['experience']=user_info.experience
        user['freetime']=user_info.freetime
        user['province']=user_info.province
        user['city'] = user_info.city
        user['country'] = user_info.country
        res = {'code': 200, 'msg': "获取成功", 'user_msg': user,"signup_msg":signupser}
        return jsonify(res)



    def post(self):
        resp={'code':200,'msg':'修改成功'}
        dict = request.form
        return jsonify(resp)


# 帖子收藏
class app_collection(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
    def get(self):
        data = self.parser.parse_args()
        id = int(data.get('id'))
        jzkcollect_infos=JzkCollect.query.filter_by(uid=id).all()
        jzkcollect={}
        jzkcollects=[]
        for jzkcollect_info in jzkcollect_infos:
            jzkcollect['pid']=jzkcollect_info.pid
            jzkcollect['title']=JzkPost.query.filter_by(id=jzkcollect['pid']).first().title
            jzkcollect['time']=jzkcollect_info.time
            jzkcollects.append(jzkcollect)
            jzkcollect={}
        res = {'code': 0, 'msg': "获取成功", 'count': JzkCollect.query.filter_by(uid=id).count(), 'data': jzkcollects}
        return jsonify(res)

    def post(self):
        reqs = {'code': 200, 'msg': '收藏成功', 'data': {}}
        dict = request.form
        uid = session['uid']
        jzkcollect_infos = JzkCollect.query.filter_by(uid=uid).all()
        for jzkcollect_info in jzkcollect_infos:
            if dict['pid'] == str(jzkcollect_info.pid):
                reqs['msg'] = "您已经收藏，请勿重复收藏"

                return jsonify(reqs)
        collect=JzkCollect(
            uid=uid,
            pid=dict['pid']
        )

        db.session.add(collect)
        db.session.commit()
        return jsonify(reqs)

    def delete(self):
        pass


# 立即报名
class enroll(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
    def get(self):
        data = self.parser.parse_args()
        id = int(data.get('id'))
        jzkcollect_infos=JzkCollect.query.filter_by(uid=id).all()
        jzkcollect={}
        jzkcollects=[]
        for jzkcollect_info in jzkcollect_infos:
            jzkcollect['pid']=jzkcollect_info.pid
            jzkcollect['time']=jzkcollect_info.time
            jzkcollects.append(jzkcollect)
            jzkcollect={}
        res = {'code': 0, 'msg': "获取成功", 'count': JzkCollect.query.filter_by(uid=id).count(), 'data': jzkcollects}

        return jsonify(res)


    def post(self):
        reqs = {'code': 200, 'msg': '报名成功', 'data': {}}
        dict = request.form
        uid = session['uid']
        jzksignup_infos = JzkSignUp.query.filter_by(uid=uid).all()

        for jzksignup_info in jzksignup_infos:
            if dict['pid'] == str(jzksignup_info.pid):
                reqs['msg'] = "您已经报名，请勿重复报名"
                return jsonify(reqs)

        signup=JzkSignUp(
            uid=uid,
            pid=dict['pid'],
            is_confirme=1
        )

        db.session.add(signup)
        db.session.commit()
        return jsonify(reqs)

    def delete(self):
        pass














api.add_resource(userMessage,"/api/userMessage/")
api.add_resource(userGroup,"/api/userGroup/")
api.add_resource(part_time,"/api/part_time/")
api.add_resource(sign_up,"/api/sign_up/")
api.add_resource(inform,"/api/inform/")
api.add_resource(advertising,"/api/advertising/")


api.add_resource(app_posts,"/api/app_posts/")
api.add_resource(business,"/api/business/")
api.add_resource(app_detal,"/api/getdetal/")
api.add_resource(app_me,"/api/getme/")
api.add_resource(app_user_message,"/api/getmemessages/")
api.add_resource(app_collection,"/api/getcollect/")
api.add_resource(enroll,"/api/getenroll/")






class te(Resource):
    def get(self):
        a="dsfsdfdsfdfsfs"
        resp = make_response(a, '200')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


api.add_resource(te,"/api/te")






