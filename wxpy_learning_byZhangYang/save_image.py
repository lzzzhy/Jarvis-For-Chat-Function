from wxpy import *
import os
import re

def safe_file_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"              # 文件名中的非法字符
    new_title = re.sub(rstr, "_", title)        # 替换为下划线
    return new_title

bot = Bot(cache_path=True)
bot.enable_puid()

image_dir = "image"

if not os.path.exists(image_dir):
    os.mkdir(image_dir)

for chat in bot.chats():
    chat_name = chat.name
    print(chat.puid)
    print("开始下载'{}'的头像".format(chat_name))

    try:
        image = chat.get_avatar()
        save_path = os.path.join(image_dir, safe_file_title(chat_name)+".jpg")

        with open(save_path, "wb") as f:
            f.write(image)
    except:
        print("获取失败")
        