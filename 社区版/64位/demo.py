# 如果你是Python36。请删除37、38、39的pyd文件，其他版本同理
from WeChatPYAPI import WeChatPYApi

import time
import logging
from queue import Queue
import os


# 当前目录路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


logging.basicConfig(level=logging.INFO)  # 日志器
msg_queue = Queue()  # 消息队列


def on_message(msg):
    """消息回调，建议异步处理，防止阻塞"""
    print(msg)
    msg_queue.put(msg)


def on_exit(wx_id):
    """退出事件回调"""
    print("微信({})：已退出登录，请重新登录".format(wx_id))


def main():
    # 初次使用需要pip安装两个库：
    # pip install requests
    # pip install pycryptodomex

    # 查看帮助
    help(WeChatPYApi)

    # 实例化api对象【要多开的话就实例化多个《WeChatPYApi》对象】
    w = WeChatPYApi(msg_callback=on_message, exit_callback=on_exit, logger=logging)

    # 调试模式：
    # debug_pid=日志中输出的进程pid
    # 注意：你的微信必须使用start_wx方法登录成功后，才能使用调试模式
    # w = WeChatPYApi(msg_callback=on_message, exit_callback=on_exit, logger=logging, debug_pid=8256)

    # 启动微信【调试模式可不调用该方法】
    errno, errmsg = w.start_wx()
    # errno, errmsg = w.start_wx(path=os.path.join(BASE_DIR, "login_qrcode.png"))  # 保存登录二维码
    if errno != 0:
        print(errmsg)
        if errmsg != "当前为调试模式，不需要调用“start_wx”":
            return

    # 这里需要阻塞，等待获取个人信息
    while not w.get_self_info():
        time.sleep(2)

    my_info = w.get_self_info()
    print("登陆成功！")
    print(my_info)

    # 拉取列表（好友/群/公众号等）第一次拉取可能会阻塞，可以自行做异步处理
    # 好友列表：pull_type = 1
    # 群列表：pull_type = 2
    # 公众号列表：pull_type = 3
    # 其他：pull_type = 4
    lists = w.pull_list(pull_type=1)
    print(lists)

    # 获取群成员列表
    # lists = w.get_chat_room_members(to_chat_room="123@chatroom")
    # print(lists)

    # 发送文本消息
    w.send_text(to_wx="filehelper", msg='作者QQ:\r437382693')
    time.sleep(1)

    # 发送图片消息
    # w.send_img(to_wx="filehelper", path=r"C:\1.png")
    # time.sleep(1)

    # 发送卡片链接
    w.send_card_link(
        to_wx="filehelper",
        title="QQ",
        desc="437382693",
        target_url="http://www.baidu.com",
        img_url="https://img.alicdn.com/bao/uploaded/TB1AptvRKH2gK0jSZJnXXaT1FXa.png_310x310.jpg"
    )

    # 处理消息回调
    while True:
        msg = msg_queue.get()

        # 收款
        if msg["msg_type"] == 490:
            is_recv = msg["detail"]["is_recv"]
            if is_recv:
                # 收款
                w.collection(msg_data=msg)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os._exit(1)

