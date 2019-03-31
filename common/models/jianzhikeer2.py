# coding: utf-8
from application import db

# 广告
class JzkAdvertising(db.Model):
    __tablename__ = 'jzk_advertising'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(500))
    link = db.Column(db.String(500))
    time = db.Column(db.DateTime, server_default=db.FetchedValue())


# 收藏
class JzkCollect(db.Model):
    __tablename__ = 'jzk_collects'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    time = db.Column(db.DateTime, server_default=db.FetchedValue())

# 反馈
class JzkFeedback(db.Model):
    __tablename__ = 'jzk_feedback'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    content = db.Column(db.String(800))

# 信息
class JzkInform(db.Model):
    __tablename__ = 'jzk_inform'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    time = db.Column(db.DateTime, server_default=db.FetchedValue())


# 商家
class JzkIsMerchant(db.Model):
    __tablename__ = 'jzk_is_merchant'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(255))
    address = db.Column(db.String(300))
    detail = db.Column(db.String(500))
    people_name = db.Column(db.String(50))
    people_tel = db.Column(db.String(11))
    lincese = db.Column(db.String(500))
    grade = db.Column(db.Integer, server_default=db.FetchedValue())
    is_vip = db.Column(db.Integer, server_default=db.FetchedValue())
    is_check = db.Column(db.Integer, server_default=db.FetchedValue())

# 兼职类型
class JzkJianzhiType(db.Model):
    __tablename__ = 'jzk_jianzhi_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

# 发帖
class JzkPost(db.Model):
    __tablename__ = 'jzk_posts'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    title = db.Column(db.String(100))
    people_tel = db.Column(db.String(255))
    people = db.Column(db.String(255))
    content = db.Column(db.String(2000))
    wages = db.Column(db.String(10))
    benefits = db.Column(db.String(50))
    need_num = db.Column(db.String(10))
    start_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    end_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    addres = db.Column(db.String(255))
    other = db.Column(db.String(500))
    is_top = db.Column(db.Integer, server_default=db.FetchedValue())
    is_check = db.Column(db.Integer, server_default=db.FetchedValue())
    is_completed = db.Column(db.Integer, server_default=db.FetchedValue())
    jianzhi_type = db.Column(db.ForeignKey('jzk_jianzhi_type.name'), index=True)
    jianzhi_time_type = db.Column(db.String(255))
    public_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    count_down_time = db.Column(db.DateTime)

    jzk_jianzhi_type = db.relationship('JzkJianzhiType', primaryjoin='JzkPost.jianzhi_type == JzkJianzhiType.name', backref='jzk_posts')


#
class JzkSignUp(db.Model):
    __tablename__ = 'jzk_sign_up'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    pid = db.Column(db.Integer)
    is_confirme = db.Column(db.Integer, server_default=db.FetchedValue())
    is_sign_in = db.Column(db.Integer, server_default=db.FetchedValue())
    is_complete = db.Column(db.Integer, server_default=db.FetchedValue())

# 用户
class JzkUser(db.Model):
    __tablename__ = 'jzk_user'

    uid = db.Column(db.Integer, primary_key=True)
    unionid = db.Column(db.Integer)
    openid = db.Column(db.Integer)
    nickname = db.Column(db.String(50))
    sex = db.Column(db.String(20))
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    avator = db.Column(db.String(255))
    account = db.Column(db.String(255))
    password = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    address = db.Column(db.String(255))
    tel = db.Column(db.String(12))
    mail = db.Column(db.String(50))
    name = db.Column(db.String(255))
    experience = db.Column(db.String(500))
    freetime = db.Column(db.String(255))
    payzhifubao = db.Column(db.String(255))
    education = db.Column(db.String(255))
    qqnum = db.Column(db.Integer)
    credit = db.Column(db.Integer, server_default=db.FetchedValue())
    group = db.Column(db.ForeignKey('jzk_user_groups.name'), index=True)
    is_merchant = db.Column(db.Integer, server_default=db.FetchedValue())

    jzk_user_group = db.relationship('JzkUserGroup', primaryjoin='JzkUser.group == JzkUserGroup.name', backref='jzk_users')

# 用户组
class JzkUserGroup(db.Model):
    __tablename__ = 'jzk_user_groups'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(255), index=True)

# 微信
class JzkWxUser(db.Model):
    __tablename__ = 'jzk_wx_user'

    uid = db.Column(db.Integer, primary_key=True)
    unionid = db.Column(db.String(255))
    openid = db.Column(db.String(255))
    nickname = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    avator = db.Column(db.String(255))



