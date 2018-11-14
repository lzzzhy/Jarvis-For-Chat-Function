# -*- coding: utf-8 -*-
import time
import os
import json

USER_ID = "13038011192"
MESSAGE_SAVE_DIR = "qqbot_message"

def get_current_time():
    '''
    返回当前时间的字符串
    '''
    return str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))


def send_short_message(phonenumber, content):
    print("向{}发送{}".format(phonenumber, content))

def save_qq_buddy_message(user_id, buddy, content):
    save_dir = os.path.join(MESSAGE_SAVE_DIR, user_id)
    print("{}  {}".format(os.getcwd(), save_dir))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    json_path = os.path.join(save_dir, 'buddy.json')

    if os.path.exists(json_path):
        print("[ ]读取中")
        with open(json_path, encoding='utf-8') as json_f:
            messages = json.load(json_f)

        messages.append([buddy.nick, get_current_time(), content])

        with open(json_path, "w", encoding='utf-8') as json_f:
            json.dump(messages, json_f, indent=4, separators=(',', ': '), ensure_ascii=False)

        print("[+]写入成功")
    else:
        messages = [[buddy.nick, get_current_time(), content]]

        with open(json_path, "w", encoding='utf-8') as json_f:
            json.dump(messages, json_f, indent=4, separators=(',', ': '), ensure_ascii=False)

        print("[+]写入成功")


def save_qq_group_message(user_id, group, member, content):
    pass

def onQQMessage(bot, contact, member, content):
    '''
    接收到消息时的处理过程
    要发送信息时可以使用bot.SendTo(contact, '内容')
    要关闭机器人时可以使用bot.Stop()

    若要查看QQ号可以使用bot.session.uin

    判断是否是自己发送的消息使用if bot.isMe(contact, member):

    判断自己是否被@可以使用：if '@ME' in content:

    发送消息使用bot.SendTo(contact, content, resendOn1202=True)
    若发送成功，返回字符串（向 xx 发消息成功）。否则，返回含错误原因的字符串（错误：...）
    发消息时可能会重复发消息，这是因为 QQ 服务器返回代码 1202 的原因
    若此参数为True，则发消息时如果QQ服务器返回代码1202（表明发消息可能失败），还会继续发送3次直至返回代码0

    :param bot: 接受的机器人
    :param contact: 对象 群or好友
    :param member: 收到群消息时的群成员
    :param content: 聊天内容
    :return:
    '''

    # 如果是自己发的信息 忽略
    if bot.isMe(contact, member):
        return

    # 当有人@时
    if '@ME' in content:
        send_short_message(13038011192, '有人@你了')

    # 如果是讨论组或者群的消息
    if member:
        save_qq_group_message(USER_ID, contact, member, content)
    # 如果是单个好友发来的消息
    else:
        save_qq_buddy_message(USER_ID, contact, content)
