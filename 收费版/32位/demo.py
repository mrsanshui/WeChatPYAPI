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
    print("已退出：{}".format(wx_id))


def main():
    # 初次使用需要pip安装三个库：
    # pip install requests
    # pip install pycryptodomex
    # pip install psutil
    #
    # 查看帮助
    help(WeChatPYApi)

    # 实例化api对象
    w = WeChatPYApi(msg_callback=on_message, exit_callback=on_exit, logger=logging)

    # 启动微信
    w.start_wx()
    # w.start_wx(path=os.path.join(BASE_DIR, "login_qrcode.png"))  # 保存登录二维码

    # 这里需要阻塞，等待获取个人信息
    while not w.get_self_info():
        time.sleep(5)

    my_info = w.get_self_info()
    self_wx = my_info["wx_id"]
    print("登陆成功！")
    print(my_info)

    # 开启保存语言【需要在登录成功后调用】
    # 保存的语音为silk文件，可使用群文件中的转换工具，批量转为mp3格式
    w.save_voice_switch(
        self_wx=self_wx,
        save_dir_path=os.path.join(BASE_DIR, "temp"),
        switch=True,
    )

    # 拉取列表（好友/群/公众号等）第一次拉取可能会阻塞，可以自行做异步处理
    # 好友列表：pull_type = 1
    # 群列表：pull_type = 2
    # 公众号列表：pull_type = 3
    # 其他：pull_type = 4
    lists = w.pull_list(self_wx=self_wx, pull_type=1)
    print(lists)

    # 获取群成员列表
    # lists = w.get_chat_room_members(self_wx=self_wx, to_chat_room="123@chatroom")
    # print(lists)

    # 拉取企业微信列表（好友/群）
    # data = w.pull_list_of_work(self_wx=self_wx)
    # print(data)

    # 获取企业群成员列表
    # lists = w.get_chat_room_members_of_work(self_wx=self_wx, to_chat_room="123@im.chatroom")
    # print(lists)

    # # 发送文本消息
    # w.send_text(self_wx=self_wx, to_wx="filehelper", msg='作者QQ:\r437382693')
    # time.sleep(1)
    #
    # # 发送图片消息
    # w.send_img(self_wx=self_wx, to_wx="filehelper", path=r"C:\1.png")
    # time.sleep(1)
    #
    # # 发送文件/视频
    # w.send_file(self_wx=self_wx, to_wx="filehelper", path=r"C:\1.mp3")
    # time.sleep(1)
    #
    # # 发送好友名片
    # w.send_friend_card(
    #     self_wx=self_wx,
    #     to_wx="filehelper",
    #     friend_wx=self_wx,
    #     friend_name="三水君"
    # )
    # time.sleep(1)
    #
    # # 发送卡片链接
    # w.send_card_link(
    #     self_wx=self_wx,
    #     to_wx="filehelper",
    #     title="QQ",
    #     desc="437382693",
    #     target_url="http://baidu.com",
    #     img_url="http://img-haodanku-com.cdn.fudaiapp.com/oimg_643855036504_1627291311.jpg_310x310.jpg"
    # )
    # time.sleep(1)
    #
    # 发送小程序【XML字段可以从消息回调中捕获，具体想怎么玩，请自行研究】
    # 注意：发送小程序时，要把xml中的发送者wx_id修改为自身的wx_id
    # w.send_small_app(
    #     self_wx=self_wx,
    #     to_wx="filehelper",
    #     img_path=os.path.join(BASE_DIR, "1.png"),
    #     xml_str=xml_str,
    # )
    # time.sleep(1)

    # 处理消息回调
    while True:
        msg = msg_queue.get()

        if msg["msg_type"] == 37:
            # 同意添加好友申请
            w.agree_friend(self_wx=self_wx, msg_data=msg)

        # 处理图片消息
        elif msg["msg_type"] == 3:
            file_path, file_name = os.path.split(msg["file_path"])
            if file_name.endswith("dat"):
                file_name = file_name.replace(".dat", "")

                # 保存图片
                w.save_img(
                    self_wx=self_wx,
                    save_path=os.path.join(BASE_DIR, "temp\\{}.png".format(file_name)),
                    msg_data=msg,
                )

        # 收款
        elif msg["msg_type"] == 490:
            is_recv = msg["detail"]["is_recv"]
            if is_recv:
                # 收款
                w.collection(self_wx=self_wx, msg_data=msg)

                # 退款
                # w.refund(self_wx=self_wx, msg_data=msg)

        # 同意好友邀请进群
        elif msg["msg_type"] == 491:
            w.agree_friend_invite_join_chat_room(self_wx=self_wx, msg_data=msg)


if __name__ == '__main__':
    main()

