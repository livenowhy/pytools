#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@data: 2022/9/16
"""

import datetime


class FuncTimer(object):
    """
    获取执行时间的上下文管理器
    """

    def __init__(self):
        self.start = None
        self.end = None
        self.cost = 0

    def __enter__(self):
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        self.cost = (self.end - self.start).total_seconds()