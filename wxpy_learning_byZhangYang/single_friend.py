from wxpy import *
import os
import re
import time
import random

def safe_file_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"              # 文件名中的非法字符
    new_title = re.sub(rstr, "_", title)        # 替换为下划线
    return new_title

bot = Bot()
bot.enable_puid()

single_friend_dir = "single_friend"

if not os.path.exists(single_friend_dir):
    os.mkdir(single_friend_dir)


for friend in bot.friends():
    chat_name = friend.name
    # print(friend.puid)
    print(chat_name)
    time.sleep(random.uniform(0.1, 0.2))
    friend.send_msg(" ॣ ॣ ॣ")
