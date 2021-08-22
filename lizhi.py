# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 13/08/2021 19:46
# @Author  : Xueli
# @File    : lizhi_alert.py
# @Software: PyCharm

# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 08/08/2021 09:17
# @Author  : Xueli
# @File    : lizhi.py.py
# @Software: PyCharm

import argparse
import requests
import re
import time
from datetime import datetime
import  pytz
import subprocess
import pandas as pd
from requests.adapters import HTTPAdapter
from langdetect import detect
# from requests.packages.urllib3.util.retry import Retry



def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


parser = argparse.ArgumentParser()
parser.add_argument(
    '-id', '--liveid', dest='liveid', type=str, required=True,
    help='The liveid of the lizhi host'
)
parser.add_argument(
    '-c', '--count-only', dest='count_only', action='store_true',
    help='Only inform the count of messages.'
)
args = parser.parse_args()


liveid = args.liveid
# 添加头部信息，伪装手机浏览器访问该URL
header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
msg_time = int(time.time() * 1000)

session = requests.Session()
# session.keep_alive = False
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', HTTPAdapter(max_retries=500))
session.mount('https://', HTTPAdapter(max_retries=500))

while True:
    # time.sleep(5)
    url=f"https://appweb.lizhi.fm/live/comments?liveId={liveid}&start={msg_time}&count=50"
    # print(url)
    # res = requests.get(url,headers=header)
    res = session.get(url, headers = header, timeout = 1)
    try:
        # print('starting reading comments')
        json_res = res.json()
        # print('finished reading comments')
    except Exception as e:
        print(f"Failed to read comments: {e}")
        # print(res.text)
        continue

    msg_time = json_res['comments']['end']
    msg_count = len(json_res['comments']['list'])

    # 整点报时
    amsterdam_dt = datetime.now()
    tz = pytz.timezone('Asia/Shanghai')
    beijing_tz = datetime.now(tz)
    beijing_dt = beijing_tz.strftime("%Y-%m-%d %H:%M:%S")
    daily_msg = \
        '多肉出没的时间是北京时间凌晨四点到凌晨五点，所以现在由小管家我接管多肉的世界，我可以讲粤语、韩语和日语的啦，详细操作可以看直播间的公告。'
    # daily_msg = ' '
    while True:
        if beijing_dt[14:16] == '00':
            if beijing_dt[17:19] == '00':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '01':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '02':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '03':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '04':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '05':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '06':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '07':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '08':
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            if beijing_dt[17:19] == '09':
                print('整点报时' + beijing_dt)
                welcome_msg = f"小管家滴滴报时，现在是北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家滴滴报时，宜家系北京时间 {beijing_dt} 秒，欢迎大家来到多肉的世界，{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break
            break
        else:
            break


    # 播报弹幕数
    if args.count_only and msg_count > 0:
        speak_msg = f"你收到了 {msg_count} 条消息."
        cmd = ["say", "-v", "Mei-Jia", "-r", "250", speak_msg]
        subprocess.call(cmd)

    # 播报弹幕内容
    else:
        # 从服务器返回的json对象获取每一条弹幕消息，并按照不同的规则“播报”弹幕消息
        for msg in json_res['comments']['list']:
            # 获取每一条弹幕消息的用户名和弹幕内容
            user_name = deEmojify(msg['userName'])
            if not user_name.strip():
                user_name = f"{user_name} 个空白"
            comment = msg['comment']

            # 给多肉号船员换个昵称
            name_df = pd.read_csv('nickname.csv', header = 0)
            nickname = name_df.set_index('name')['nick_name'].to_dict()
            for k,v in nickname.items():
                if k in user_name:
                    user_name = v

            # 定义弹幕消息的播报内容
            speak_msg = f"{user_name} 说: {comment}"
            speak_username = f"{user_name} 说:"

            # 欢迎多肉号成员回家
            if user_name in nickname.values() and speak_msg.__contains__('欢迎'):
                welcome_msg = f"小管家欢迎 {user_name} 回到多肉号。{daily_msg}"
                time_msg = time.asctime()
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                welcome_msg = f"小管家欢迎 {user_name} 返来多肉号。{daily_msg}"
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                break

            # 欢迎过客来到多肉的世界
            if speak_msg.__contains__('欢迎'):
                welcome_msg = f"小管家欢迎 {user_name} 来到多肉的世界。"
                custom_msg = f"{user_name} 你好哇！{daily_msg} "
                time_msg = time.asctime()
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", welcome_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", welcome_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", custom_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Sin-ji", "-r", "190", custom_msg]
                subprocess.call(cmd)
                break

            # 过滤弹幕消息，如果弹幕中包含以下词汇，则忽略此条弹幕
            filter_ls = ['直播间', '系统提示', '鲜花', '漂流瓶', '香槟玫瑰']
            if any(word in speak_msg for word in filter_ls):
                print('不播报此条消息: ' + speak_msg)
                break

            # 感谢大家送的礼物
            if speak_msg.__contains__('为 多肉的世界🌱🌲 开出'):
                thank_msg = f"哇！小管家十分感谢 {user_name} 给多肉送的礼物，多谢支持喔。"
                can_thank_msg = f"哇！唔该晒 {user_name} 送卑多肉嘅礼物，小管家表示，多谢佬细。"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", thank_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", can_thank_msg]
                subprocess.call(cmd)
                break

            if speak_msg.__contains__('给  多肉的世界🌱🌲  送了'):
                thank_msg = f"哇！小管家十分感谢 {user_name} 给多肉送的礼物，多谢支持喔。"
                can_thank_msg = f"哇！唔该晒 {user_name} 送卑多肉嘅礼物，小管家表示，多谢佬细。"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "190", thank_msg]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", can_thank_msg]
                subprocess.call(cmd)
                break


            # 检测评论的语言，根据检测结果使用不同语言播报
            try:
                comment_lang = detect(comment)
            except Exception as e:
                print(f"No features in text: {e}")
                comment_lang = 'zh-cn'
                continue
            if comment_lang == 'zh-cn':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'ja':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Kyoko", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'ko':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Yuna", "-r", "170", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'en':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Victoria", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'nl':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Xander", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'fr':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Thomas", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'es':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Monica", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment_lang == 'de':
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Anna", "-r", "180", speak_comment]
                subprocess.call(cmd)
            elif comment.__contains__('!cantonese'):
                speak_comment = comment.replace("!cantonese", " ")
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Sin-ji", "-r", "180", speak_msg]
                subprocess.call(cmd)
            else:
                print('do not support this language now, use default language Chinese!')
                print(comment_lang + ':' + comment)
                speak_comment = f"{comment}"
                time_msg = time.asctime()
                print(time_msg, speak_msg)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_username]
                subprocess.call(cmd)
                cmd = ["say", "-v", "Mei-Jia", "-r", "180", speak_comment]
                subprocess.call(cmd)