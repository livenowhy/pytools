#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: lzp
@contact: liuzhangpei@126.com
@func: 时间处理, utc 时间转化成本地时间
"""

import pytz
import time


from gcommon.utils.time.ctime import str_to_stamp






def tz_utc_str_to_local_str(string_time='2020-12-02T07:04:00.863Z'):
    """
    :param string_time: 对 2020-12-02T07:04:00.863Z utc 时间字符串进行处理
    """
    if len(string_time) < 19:
        raise Exception('tz_utc_str_to_local_str 时间格式不对')
    string_time = string_time[:19].replace('T', ' ')
    return utc_str_to_local_str(string_time=string_time)


def local_str_to_utc_str(string_time='2019-5-10 23:40:00', format='%Y-%m-%d %H:%M:%S',
                         time_zone=8*60*60, out_format='%Y-%m-%d %H:%M:%S'):
    """
    :param string_time: utc 字符串时间
    :param utc_format: 字符串格式
    :param time_zone: 本地时区
    :return: 本地字符串时间 -> utc 字符串时间
    """
    timestamp = str_to_stamp(string_time=string_time, utc_format=format)
    timestamp = timestamp - time_zone
    return local_stamp_to_str(timestamp=timestamp, format=out_format)



def stamp_to_time(stamp):
    datatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(str(stamp)[0:10])))
    datatime = datatime + '.' + str(stamp)[10:]
    return datatime