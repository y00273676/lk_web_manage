#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, TEXT, DATETIME
from orm.base import NotNullColumn, Base, ModelBase
from lib.decorator import model_to_dict, models_to_list, close_conn
from const import DB_SOFTDOG
from sqlalchemy.sql.expression import func
import datetime
from sqlalchemy import Column
from sqlalchemy.sql.expression import func, desc, asc, or_

class SoftDog(Base):
    '''
    分类数据管理
    '''
    __tablename__ = 'ktv_softdog'

    ktv_id = Column(INTEGER(11), primary_key=True)
    ktv_name = NotNullColumn(VARCHAR(128), default='')
    ktv_subname = NotNullColumn(VARCHAR(128), default='')
    province_id = NotNullColumn(INTEGER(11), default=0)
    city_id = NotNullColumn(INTEGER(11), default=0)
    county  = NotNullColumn(VARCHAR(128), default='')
    ktv_count = NotNullColumn(TINYINT, default=0)
    ktv_box = NotNullColumn(TINYINT, default=0)
    pay_count = NotNullColumn(TINYINT, default=0)
    meal_type = NotNullColumn(TINYINT, default=0)
    base_module = NotNullColumn(TINYINT, default=0)
    link_module = NotNullColumn(TINYINT, default=0)
    mobile_module = NotNullColumn(TINYINT, default=0)
    third_status = NotNullColumn(TINYINT, default=0)
    address = Column(TEXT)
    contacts = NotNullColumn(VARCHAR(128), default='')
    moblie_no = NotNullColumn(VARCHAR(64), default='')
    welcome = NotNullColumn(VARCHAR(512), default='')
    room_text = NotNullColumn(VARCHAR(128), default='')
    city_status = NotNullColumn(TINYINT, default=0)
    agent_check = NotNullColumn(TINYINT, default=0)
    agent_fail = Column(TEXT)
    bussiness_check = NotNullColumn(TINYINT, default=0)
    bussiness_fail = Column(TEXT)
    box_change = Column(TEXT)


class Agent(ModelBase):
    """用户设备信息"""

    __tablename__ = 'ktv_agent'

    agent_id = Column(INTEGER(11), primary_key=True)
    contacts = Column(VARCHAR(64))
    mobile_no = Column(VARCHAR(128))
    mail = Column(VARCHAR(128))
    agent_no = Column(VARCHAR(256))
    starttime = Column(DATETIME)
    endtime = Column(DATETIME)
    province = Column(TEXT)
    city = Column(VARCHAR(64))
    class_user = Column(TINYINT)
    username = Column(VARCHAR(64))
    passwd = Column(VARCHAR(64))


class APIModel(object):
    def __init__(self , pdb):
        self.pdb = pdb
        self.master = pdb.get_session(DB_SOFTDOG, master=True)
        self.slave = pdb.get_session(DB_SOFTDOG)

