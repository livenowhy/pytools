#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@data: 2022/10/28
"""


from loguru import logger
import pytz
import time
from datetime import datetime


def str_to_stamp(string_time='2019-5-10 23:40:00', utc_format='%Y-%m-%d %H:%M:%S'):
    """
    :param string_time: 2018-09-19 22:10:38
    :param utc_format: 字符串时间格式
    :return: 字符串时间转换成 utc 时间戳 (2018-09-19 22:10:38 -> 1557502800)
    """
    time_array = time.strptime(string_time, utc_format)  # 先转换为时间数组
    time_stamp = int(time.mktime(time_array))            # 转换为时间戳
    return time_stamp

def local_stamp_to_str(timestamp=None, format='%Y-%m-%d %H:%M:%S'):
    """
    :param timestamp: None:返回当前时间的字符串格式 (本地时间)
    :return: 时间戳 --> 时间字符串 2018-09-19 22:10:38
    """
    if timestamp is None:
        timestamp = int(time.time())

    if isinstance(timestamp, int) is False:
        raise Exception('timestamp not int')
    timestruct = time.localtime(timestamp)
    return time.strftime(format, timestruct)

def utc_str_to_local_str(string_time='2019-5-10 23:40:00', format='%Y-%m-%d %H:%M:%S', time_zone=8*60*60):
    """
    :param string_time: utc 字符串时间
    :param utc_format: 字符串格式
    :param time_zone: 本地时区
    :return: utc 字符串时间 -> 本地字符串时间
    """
    timestamp = str_to_stamp(string_time=string_time, utc_format=format)
    timestamp = timestamp + time_zone
    return local_stamp_to_str(timestamp=timestamp, format=format)