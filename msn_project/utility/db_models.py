import datetime
from flask_sqlalchemy import SQLAlchemy
from msn_project.my_application import app

db = SQLAlchemy(app)


class Duomai_detail(db.Model):
    __tablename__ = 'duomai_report_details'

    id = db.Column(db.Integer, primary_key=True)
    vip_id = db.Column(db.Integer, nullable=False)
    website_id = db.Column(db.Integer, nullable=False)
    activity_id = db.Column(db.String(50), nullable=False)
    # 订单时间
    order_time = db.Column(db.TIMESTAMP, nullable=False)
    feedback_label = db.Column(db.String(30), nullable=True)
    order_number = db.Column(db.String(30), nullable=False)
    intention_order_number = db.Column(db.Integer, nullable=False)
    intention_order_amount = db.Column(db.DECIMAL)
    intention_commission = db.Column(db.DECIMAL)
    confirmed_order_number = db.Column(db.Integer)
    confirmed_order_amount = db.Column(db.DECIMAL)
    confirmed_commission = db.Column(db.DECIMAL)
    performance_status = db.Column(db.String(20), nullable=False)
    performance_confirmed_time = db.Column(db.TIMESTAMP)
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    modify_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self):
        self.create_time = datetime.utcnow()
        self.modify_time = datetime.utcnow()

    def __repr__(self):
        return '<Duomai_detail %s>' % self.__tablename__


class JD_detail(db.Model):
    __tablename__ = 'jd_commission_details'

    id = db.Column(db.Integer, primary_key=True)
    # 时间
    promotion_date = db.Column(db.TIMESTAMP, nullable=False)
    # 业务类型
    business_type = db.Column(db.String(20), nullable=True)
    # 推广渠道
    promotion_channels = db.Column(db.String(50), nullable=False)
    # 佣金类型
    type = db.Column(db.String(30), nullable=True)
    # 金额
    amount = db.Column(db.DECIMAL)
    # 全部结算状态/已结算/未结算
    billing_status = db.Column(db.String(20), nullable=False)
    # 记录创建时间
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    # 记录最后一次修改时间
    modify_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self):
        self.create_time = datetime.utcnow()
        self.modify_time = datetime.utcnow()

    def __repr__(self):
        return '<JD_detail %s>' % self.__tablename__


class Taobao_detail(db.Model):
    __tablename__ = 'taobao_product_effect'

    id = db.Column(db.Integer, primary_key=True)
    # 时间
    promotion_date = db.Column(db.TIMESTAMP, nullable=False)
    # 推广位
    promotion_bit = db.Column(db.String(50), nullable=False)
    # 点击数
    clicks = db.Column(db.Integer, nullable=False)
    # 付款笔数
    payments = db.Column(db.Integer, nullable=False)
    # 预估效果
    effects = db.Column(db.String(50), nullable=True)
    # 预估收入
    revenue = db.Column(db.DECIMAL, nullable=True)
    # 记录创建时间
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    # 记录最后一次修改时间
    modify_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self):
        self.create_time = datetime.utcnow()
        self.modify_time = datetime.utcnow()

    def __repr__(self):
        return '<Taobao_detail %s>' % self.__tablename__
