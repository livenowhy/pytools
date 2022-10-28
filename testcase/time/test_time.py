#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@data: 2022/10/28
"""

from loguru import logger
import pytest

from pytools.time.format import str_to_stamp


class TestTime(object):
    @pytest.mark.time
    def test_str_to_stamp(self):
        """ 字符串时间转换成 utc 时间戳 """
        time_stamp = str_to_stamp()
        assert 1557502800 == time_stamp

