import argparse
import requests
import re
import time
import subprocess


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
    '-u', '--url', dest='url', type=str, required=True,
    help='The url shared from lizhi'
)
parser.add_argument(
    '-c', '--count-only', dest='count_only', action='store_true',
    help='Only inform the count of messages.'
)
args = parser.parse_args()


live_url = args.url
liveid = re.search(r'liveId=(\d+)', live_url).group(1)

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
    if args.count_only and msg_count > 0:
        speak_msg = f"你收到了 {msg_count} 条消息."
        cmd = ["say", "-v", "Mei-Jia", "-r", "200", speak_msg]
        subprocess.call(cmd)

    else:
        for msg in json_res['comments']['list']:
            user_name = deEmojify(msg['userName'])
            if not user_name.strip():
                user_name = f"{user_name} 个空白"
            comment = msg['comment']
            speak_msg = f"{user_name} 说: {comment}"
            cmd = ["say", "-v", "Mei-Jia", "-r", "200", speak_msg]
            subprocess.call(cmd)

