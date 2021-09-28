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
    # xml_str = '<?xml version="1.0"?>\n<msg>\n\t<appmsg appid="" sdkver="0">\n\t\t<title>这些电影预告片你都看了吗？</title>\n\t\t<des>猫眼电影演出I电影票演唱会话剧</des>\n\t\t<action />\n\t\t<type>33</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url>https://mp.weixin.qq.com/mp/waerrpage?appid=wxdbb4c5f1b8ee7da1&amp;type=upgrade&amp;upgradetype=3#wechat_redirect</url>\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<songalbumurl />\n\t\t<songlyric />\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<emoticonmd5 />\n\t\t\t<fileext />\n\t\t\t<cdnthumburl>3075020100046e306c02010002044a1f279d02032f5d0302041c30f0b70204615356140447777875706c6f61645f66696c6568656c706572373632385f313633323835313437355f36363934636366622d323232642d343566312d613336392d3433376464613063623637300204011800030201000400</cdnthumburl>\n\t\t\t<cdnthumbmd5>7592d8e0e7fba4ea48b83c48fab0936b</cdnthumbmd5>\n\t\t\t<cdnthumblength>109400</cdnthumblength>\n\t\t\t<cdnthumbwidth>720</cdnthumbwidth>\n\t\t\t<cdnthumbheight>576</cdnthumbheight>\n\t\t\t<cdnthumbaeskey>fba6e188363542fe88db7f28d3fc9cb1</cdnthumbaeskey>\n\t\t\t<aeskey>fba6e188363542fe88db7f28d3fc9cb1</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t\t<filekey>filehelper7628_1632851475</filekey>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername>gh_d9004ba7511f@app</sourceusername>\n\t\t<sourcedisplayname>猫眼电影演出I电影票演唱会话剧</sourcedisplayname>\n\t\t<thumburl />\n\t\t<md5 />\n\t\t<statextstr />\n\t\t<directshare>0</directshare>\n\t\t<recorditem><![CDATA[<recordinfo><edittime>0</edittime><fromscene>0</fromscene></recordinfo>]]></recorditem>\n\t\t<weappinfo>\n\t\t\t<username><![CDATA[gh_d9004ba7511f@app]]></username>\n\t\t\t<appid><![CDATA[wxdbb4c5f1b8ee7da1]]></appid>\n\t\t\t<type>2</type>\n\t\t\t<version>959</version>\n\t\t\t<weappiconurl><![CDATA[http://mmbiz.qpic.cn/mmbiz_png/uibGIIlerq8Cbjt2IdQ5tDfy9Iiae3oJ0zyllsFQlsibtBrUZFWZq2AdEoZ0BxmRQ0ltVTknCI1u4cf2M0UYkfpWw/640?wx_fmt=png&wxfrom=200]]></weappiconurl>\n\t\t\t<pagepath><![CDATA[pages/movie/index.html?utm_source=share_wallet&channelStyle=1&cityName=%E6%A2%85%E5%B7%9E&cityId=282&accessfrom=share&channelId=101&accessfrom=share&userCode=bayA8jm3D49kbpWa6vdBgV06enYQ]]></pagepath>\n\t\t\t<shareId><![CDATA[0_wxdbb4c5f1b8ee7da1_ede8ac1e955a455a86a2056970043f41_1632851475_0]]></shareId>\n\t\t\t<appservicetype>0</appservicetype>\n\t\t\t<tradingguaranteeflag>0</tradingguaranteeflag>\n\t\t\t<brandofficialflag>0</brandofficialflag>\n\t\t\t<subType>0</subType>\n\t\t\t<isprivatemessage>0</isprivatemessage>\n\t\t</weappinfo>\n\t</appmsg>\n\t<fromusername>wxid_gocm3yjflab921</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname></appname>\n\t</appinfo>\n\t<commenturl></commenturl>\n</msg>\n'
    # w.send_small_app(
    #     self_wx=self_wx,
    #     to_wx="filehelper",
    #     img_path=os.path.join(BASE_DIR, "login_qrcode.png"),
    #     xml_str=xml_str,
    # )
    # time.sleep(1)

    # 处理消息回调
    while True:
        msg = msg_queue.get()

        if msg["msg_type"] == 37:
            # 同意添加好友申请
            w.agree_friend(self_wx=self_wx, msg_data=msg)

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

