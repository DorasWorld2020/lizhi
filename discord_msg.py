# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 16/08/2021 00:21
# @Author  : Xueli
# @File    : discord_msg.py
# @Software: PyCharm

import requests
import time

dc_url = 'https://discord.com/api/v9/channels/876602173516046347/messages'
header = {
    'authorization': "Nzg3NDU0MDgzNTE4MzAwMTcx.YRmWcw.zewWCvjMkjEBew92zhLtqgW7Q7o"
}

liveid = input('pls input lizhi live ID: ')
msg_time = int(time.time() * 1000)

while True:
    url=f"https://appweb.lizhi.fm/live/comments?liveId={liveid}&start={msg_time}&count=50"
    res = requests.get(url)
    try:
        json_res = res.json()
    except Exception as e:
        print(f"Failed to read comments: {e}")
        print(res.text)
        continue
    msg_time = json_res['comments']['end']
    msg_count = len(json_res['comments']['list'])
    for msg in json_res['comments']['list']:
        user_name = msg['userName']
        comment = msg['comment']
        lizhi_msg = user_name + ': ' + comment
        payload = {
            'content': lizhi_msg
        }
        r = requests.post(dc_url, data=payload, headers=header)