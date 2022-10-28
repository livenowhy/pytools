#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: lzp
@contact: liuzhangpei@126.com
@func: 时间处理
"""

import pytz
import time
import datetime
from gcommon.utils.time.ctime import str_to_stamp

basestring = (str, bytes)



def append_tz(t, zone='Asia/Shanghai'):
    tz = pytz.timezone(zone=zone)
    return tz.localize(t)


def epoch(t):
    """ Date/Time converted to seconds since epoch """
    if not hasattr(t, 'tzinfo'):
        return
    return int(time.mktime(append_tz(t).timetuple()))


def now_compat():
    return datetime.datetime.now() - datetime.timedelta(hours=8)


def stamp_to_str(timestamp=None, format='%Y-%m-%d %H:%M:%S'):
    """
    :param timestamp: None:返回当前时间的字符串格式
    :return: 时间戳 --> 时间字符串 2018-09-19 22:10:38
    """
    if timestamp is None:
        timestamp = int(time.time())

    if isinstance(timestamp, int) is False:
        raise Exception('timestamp not int')
    timestruct = time.gmtime(timestamp)
    return time.strftime(format, timestruct)


def str_to_local(string_time, utc_format, time_zone=8 * 60 * 60):
    """ 字符串时间转换成本地的时间字符串 """
    time_stamp = str_to_stamp(string_time=string_time, utc_format=utc_format)
    time_stamp = time_stamp + time_zone
    return stamp_to_str(timestamp=time_stamp, format=utc_format)


def tz_to_utc_str(tz_str):
    """ 2020-11-27T11:06:44.287975278Z 时间转变成 utc 时间 """
    if len(tz_str) < 19:
        raise Exception('时间格式不对')
    tz_str = tz_str[0:19].replace('T', ' ')
    timestamp = str_to_stamp(string_time=tz_str)
    time_str = stamp_to_str(timestamp)

    def stampToTime(stamp):
        datatime = time.stamp_to_str("%Y-%m-%d %H:%M:%S", time.localtime(float(str(stamp)[0:10])))
        datatime = datatime + '.' + str(stamp)[10:]
        return datatime
    return time_str



def datetimetostring(date_time, format="%Y-%m-%d %H:%M:%S"):
    if isinstance(date_time, (datetime.date,)):
        return date_time.strftime(format)
    elif isinstance(date_time, (basestring,)):
        return date_time
    else:
        return date_time if date_time else ""


def str2datetime(datetime_str, format="%Y-%m-%d %H:%M:%S"):
    if isinstance(datetime_str, (basestring,)):
        return datetime.datetime.strptime(datetime_str, format)
    return datetime_str


def datetime2timestampms(datetime):
    return int(time.mktime(datetime.timetuple()))


def datetime_to_string(date, fmt='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strftime(date, fmt)

def day_begin_end_by_timestamp(timestamp=None):
    """
    :param timestamp: 某一天 任意时刻的时间戳 (秒)
    :return: 该天 00:00:00 时间戳; 到第二天 00:00:00 时间戳
    """
    time_str = stamp_to_str(timestamp=timestamp, format='%Y-%m-%d')
    begin = str_to_stamp(string_time=time_str, utc_format='%Y-%m-%d')
    end = begin + 60 * 60 * 24
    return begin, end
