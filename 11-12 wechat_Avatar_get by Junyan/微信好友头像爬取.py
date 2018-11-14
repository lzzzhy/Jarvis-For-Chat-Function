# 导入模块
from wxpy import *

# 新建机器人对象
bot = Bot(cache_path=True)

# 获取好友列表
myFriends = bot.friends()

# 输入保存路径
save_Path = input("请键入保存路径\n")

# 遍历好友列表并保存头像
for friend in myFriends:
    friend.get_avatar(save_path=save_Path+"/"+str(friend.name)+".jpg")

# 头像爬取完毕
print("您的微信好友头像已保存到", save_Path, "\n")
