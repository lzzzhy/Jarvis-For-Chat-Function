# -*- coding: utf-8 -*-
import time
import os
import json

USER_ID = "13038011192"
MESSAGE_SAVE_DIR = "qqbot_message"

def get_current_time():
    '''
    以字符串形式返回当前时间
    '''
    return str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))


def send_short_message(phonenumber, content):
    '''
    发送短信 待补充
    :param phonenumber: 手机号码
    :param content: 要发送的信息
    :return: 发送成功返回True 否则返回False
    '''
    print("向{}发送{}".format(phonenumber, content))

def save_qq_buddy_message(user_id, buddy, content):
    '''
    保存QQ好友的消息
    :param user_id:
    :param buddy:
    :param content:
    :return:
    '''
    save_dir = os.path.join(MESSAGE_SAVE_DIR, user_id)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    json_path = os.path.join(save_dir, 'buddy.json')

    if os.path.exists(json_path):
        print("[ ]读取messages.json中")
        with open(json_path, encoding='utf-8') as json_f:
            messages = json.load(json_f)

        messages.append([buddy.nick, get_current_time(), content])

        with open(json_path, "w", encoding='utf-8') as json_f:
            json.dump(messages, json_f, indent=4, separators=(',', ': '), ensure_ascii=False)

        print("[+]messages.json写入成功")
    else:
        messages = [[buddy.nick, get_current_time(), content]]

        with open(json_path, "w", encoding='utf-8') as json_f:
            json.dump(messages, json_f, indent=4, separators=(',', ': '), ensure_ascii=False)

        print("[+]messages.json写入成功")


def save_qq_group_message(user_id, group, member, content):
    '''
    保存QQ群消息
    :param user_id:
    :param group:
    :param member:
    :param content:
    :return:
    '''
    save_dir = os.path.join(MESSAGE_SAVE_DIR, user_id)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # print(member.__dict__)

    group_name = group.nick
    json_path = os.path.join(save_dir, group_name+'.json')

    # 优先保存群备注
    member_name = member.card
    if len(member_name) == 0:
        # 群备注为空时以网名保存
        member_name = member.name


    if os.path.exists(json_path):
        print("[ ]读取群\"{}\"的文件中".format(group_name))
        with open(json_path, encoding='utf-8') as json_f:
            messages = json.load(json_f)

        messages.append([group.nick, member_name, get_current_time(), content])

        with open(json_path, "w", encoding='utf-8') as json_f:
            json.dump(messages, json_f, indent=4, separators=(',', ': '), ensure_ascii=False)

        print("[ ]群\"{}\"文件写入成功".format(group_name))

    else:
        messages = [[group.nick, member_name, get_current_time(), content]]

        with open(json_path, "w", encoding='utf-8') as json_f:
            json.dump(messages, json_f, indent=4, separators=(',', ': '), ensure_ascii=False)

        print("[ ]群\"{}\"文件写入成功".format(group_name))


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

    # 如果消息长度为0(一般是图片以及文件等无法获取的消息)时忽略
    if len(content) == 0:
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
