#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@data: 2022/8/29
"""

from loguru import logger
from pytz import utc
from datetime import datetime


def make_corn_time(kwargs):
    """
    获取 corn time 时间格式
    run_date_start: 时间
    run_date_format: str 字符串时间格式(默认); corn crontab 格式 5 8 * * *
    """
    run_date_start = kwargs.get('run_date_start', None)
    if run_date_start is None:
        return None

    run_date_format = kwargs.get('run_date_format', 'str')
    if 'corn' == run_date_format:  # crontab 格式, 直接返回
        return run_date_start

    run_date_start = run_date_start.split('.')[0]
    local_time = datetime.strptime(run_date_start, '%Y-%m-%d %H:%M:%S')
    utc_time = local_time.astimezone(utc)
    corn_time = f"{utc_time.minute} {utc_time.hour} {utc_time.day} {utc_time.month} *"
    return corn_time