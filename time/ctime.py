#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: lzp
@contact: liuzhangpei@126.com
@func: 时间处理
"""


from datetime import datetime




def now_hour_begin_end():
    """
    python3
    获取整点时间戳; 比如当前时间 2020-12-29 16:38:55;
    begin: 2020-12-29 16:00:00 的时间戳
      end: 2020-12-29 17:00:00 的时间戳
    """
    begin = int(datetime.now().replace(minute=0, second=0, microsecond=0).timestamp())
    end = begin + 60 * 60
    return begin, end


def day_begin_end(date=None):
    """
    :param date: 为 None 获取当天 (20201222)
    :return: 获取一天开始和结束的时间戳;
    """
    begin = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    if date:
        date = str(date)
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        begin = datetime.now().replace(
            year=year, month=month, day=day,
            hour=0, minute=0, second=0, microsecond=0).timestamp()
    begin = int(begin)
    return begin, begin + 60 * 60 * 24

