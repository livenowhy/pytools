#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@data: 2022/10/28
@func: 时间戳
"""

import datetime
import time


def get_float_time_stamp():
    """ 当前 时间戳 """
    datetime_now = datetime.datetime.now()
    return datetime_now.timestamp()


def get_time_stamp_13():
    """ 生成 13 时间戳 """
    datetime_now = datetime.datetime.now()
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    data_microsecond = str("%06d" % datetime_now.microsecond)[0:3]  # 3位，微秒
    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


def get_time_stamp_16():
    """ 生成 16 时间戳 1606716352942310 -ln """
    datetime_now = datetime.datetime.now()
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))  # 10 位，时间点相当于从 UNIX TIME 的纪元时间开始的当年时间编号
    data_microsecond = str("%06d" % datetime_now.microsecond)     # 6 位，微秒
    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)