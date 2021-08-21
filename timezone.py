# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 18/08/2021 14:29
# @Author  : Xueli
# @File    : timezone.py
# @Software: PyCharm

from datetime import datetime
import pytz

local_dt = datetime.now()
tz = pytz.timezone('Asia/Shanghai')
beijing_dt = datetime.now(tz)
beijing_now = beijing_dt.strftime("%Y-%m-%d %H:%M:%S")

print(local_dt)
print(tz.zone)
print(beijing_now)
print(beijing_dt)