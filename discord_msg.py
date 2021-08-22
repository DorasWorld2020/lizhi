# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 16/08/2021 00:21
# @Author  : Xueli
# @File    : discord_msg.py
# @Software: PyCharm

import requests
import time
from requests.adapters import HTTPAdapter
from langdetect import detect

dc_url = 'https://discord.com/api/v9/channels/876602173516046347/messages'
header = {
    'authorization': "Nzg3NDU0MDgzNTE4MzAwMTcx.YRmWcw.zewWCvjMkjEBew92zhLtqgW7Q7o",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

liveid = input('pls input lizhi live ID:')
msg_time = int(time.time() * 1000)
session = requests.Session()
# session.keep_alive = False
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', HTTPAdapter(max_retries=500))
session.mount('https://', HTTPAdapter(max_retries=500))


while True:
    url=f"https://appweb.lizhi.fm/live/comments?liveId={liveid}&start={msg_time}&count=50"
    res = session.get(url, headers=header, timeout=4)
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
        filter_ls = ['的直播间打开', '荔枝妹', '鲜花', '漂流瓶', '香槟玫瑰', '进入直播间']
        if any(word in lizhi_msg for word in filter_ls):
            print('不播报此条消息: ' + lizhi_msg)
            break
        else:
            # print(lizhi_msg)
            payload = {
                'content': lizhi_msg
            }
            r = requests.post(dc_url, data=payload, headers=header)