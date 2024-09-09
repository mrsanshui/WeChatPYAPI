# WeChatPYAPI介绍



《WeChatPYAPI》是基于PC端的Python接口，开发者可通过Python轻松调用，也可通过HTTP调用。可进行二次开发，实现微信机器人、群管理等强大的功能！



### 社区版跟专业版的区别？

- 社区版：
  - 麻雀虽小五脏俱全！
  - 不支持长时间运行
  - 不再维护更新
  - 微信版本：3.6.0.18
- 专业版：
  - 功能更加强大、稳定！
  - 支持长时间运行
  - 持续更新迭代
  - 微信版本：3.9.10.19

> <span style="color: red">功能区别请打开《接口使用文档》进行查看</span>



> 如果对你有帮助，别吝啬你的小手留个star呗



## 使用教程

1. 克隆该项目<span style="color: red">（请关闭你的杀毒软件，否则可能会误删dll文件）</span>
2. 选择对应python解释器环境（必须是64位的）
4. 执行文件夹中的demo.py
4. 使用前请先安装指定版本的微信

> 指定版本微信安装包：https://pan.baidu.com/s/1dxBuvDgAeI0mFjGsY6NVNA
>
> 提取码：sszs



## 疑问解答、联系方式

- 交流QQ群：54995858
- tg讨论组：https://t.me/+yb0O_hNMqIVlODI1
- 进群解决一切蛇皮问题！



## 学习 & 参考

https://github.com/mrsanshui/WeChatApi.git



## help(WeChatPYApi)

```python
class WeChatPYApi(builtins.object)
 |  基于PC微信的Python-API
 |  
 |  Methods defined here:
 |  
 |  __init__(self, msg_callback, **kwargs)
 |      初始化方法
 |      :param msg_callback: 消息回调函数
 |      :param exit_callback: 退出微信后的回调函数
 |      :param logger: 日志器句柄
 |      :param kwargs: 略
 |  
 |  add_friend(self, wx_id_or_v3, msg, method=30)
 |      添加好友
 |      :param wx_id_or_v3: 要添加的微信ID或者v3数据
 |      :param msg: 添加时的打招呼消息
 |      :param method: 添加方式【默认30】
 |      :return: 无
 |  
 |  agree_friend(self, msg_data)
 |      同意添加好友请求
 |      :param msg_data: 好友请求时的消息数据
 |      :return: 无
 |  
 |  agree_friend_invite_join_chat_room(self, msg_data)
 |      同意好友邀请进群
 |      :param msg_data: 消息数据
 |      :return: 群ID
 |  
 |  alter_chat_room_name(self, to_chat_room, name)
 |      修改群名称
 |      :param to_chat_room: 群ID
 |      :param name: 群名称
 |      :return: 无
 |  
 |  alter_friend_desc(self, to_wx, desc)
 |      修改好友描述信息
 |      :param to_wx: 好友微信ID
 |      :param desc: 描述信息
 |      :return: 无
 |  
 |  alter_friend_remark(self, to_wx, remark)
 |      修改好友备注
 |      :param to_wx: 好友微信ID
 |      :param remark: 备注内容
 |      :return: 无
 |  
 |  alter_my_name_in_chat_room(self, to_chat_room, name)
 |      修改我在群里的昵称
 |      :param to_chat_room: 群ID
 |      :param name: 昵称
 |      :return: 无
 |  
 |  batch_query_member_nick_name(self, to_chat_room, wx_id_list)
 |      批量查询群成员的群昵称
 |      :param to_chat_room: 群ID
 |      :param wx_id_list: 群成员的微信ID列表
 |      :return: List数据
 |  
 |  cdn_download_file(self, file_size, file_id, aes_key, save_path)
 |      CDN下载文件
 |      :param file_size: 文件大小【消息回调中获取】
 |      :param file_id: 文件ID【消息回调中获取】
 |      :param aes_key: aes_key【消息回调中获取】
 |      :param save_path: 保存路径
 |      :return: 无
 |  
 |  cdn_download_img(self, img_type, file_id, aes_key, save_path)
 |      CDN下载图片
 |      :param img_type: 图片类型【1=缩略图 2=高清图 3=原图】
 |      :param file_id: 文件ID【消息回调中获取】
 |      :param aes_key: aes_key【消息回调中获取】
 |      :param save_path: 保存路径
 |      :return: 无
 |  
 |  cdn_download_video(self, file_id, aes_key, save_path)
 |      CDN下载视频
 |      :param file_id: 文件ID【消息回调中获取】
 |      :param aes_key: aes_key【消息回调中获取】
 |      :param save_path: 保存路径
 |      :return: 无
 |  
 |  collection(self, msg_data)
 |      收款
 |      :param msg_data: 消息数据
 |      :return: 无
 |  
 |  comment_moments(self, moments_id, content)
 |      朋友圈评论
 |      :param moments_id: 朋友圈ID
 |      :param content: 评论内容
 |      :return: 无
 |  
 |  create_chat_room(self, wx_id_list)
 |      创建群聊
 |      :param wx_id_list: 邀请进群的微信ID列表
 |      :return: 群ID
 |  
 |  del_comment_moments(self, moments_id, comment_id)
 |      朋友圈删除评论
 |      :param moments_id: 朋友圈ID
 |      :param comment_id: 评论ID
 |      :return: 无
 |  
 |  delete_chat_room_member(self, to_chat_room, to_wx_list)
 |      踢出群成员
 |      :param to_chat_room: 群ID
 |      :param to_wx_list: 群成员微信ID列表
 |      :return: 无
 |  
 |  delete_friend(self, to_wx)
 |      删除好友
 |      :param to_wx: 要删除的微信ID
 |      :return: 无
 |  
 |  exit_chat_room(self, to_chat_room)
 |      退出群聊
 |      :param to_chat_room: 群ID
 |      :return: 无
 |  
 |  follow_mp(self, mp_id)
 |      关注公众号
 |      :param mp_id: 公众号ID
 |      :return: 无
 |  
 |  forward_msg(self, to_wx, msg_id)
 |      转发任意消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param msg_id: 消息ID
 |      :return: 无
 |  
 |  get_access_url(self, url)
 |      获取外部浏览器可访问的URL
 |      :param url: 只能在微信中打开的URL（如公众号链接）
 |      :return: 可访问的URL
 |  
 |  get_chat_room_members(self, to_chat_room)
 |      获取群成员列表
 |      :param to_chat_room: 群ID
 |      :return: list数据
 |  
 |  get_cur_window_info(self)
 |      获取当前聊天窗口信息
 |      :return: dict数据
 |  
 |  get_cur_wx_pid(self)
 |      获取当前微信进程的PID
 |      :return: 进程PID
 |  
 |  get_db_name_list(self)
 |      获取所有数据库名称
 |      :return: List数据
 |  
 |  get_login_state(self)
 |      获取微信登录状态
 |      :return: True:已登录 False:未登录
 |  
 |  get_moments(self, last_id=None)
 |      获取朋友圈数据
 |      :param last_id: 最后一条朋友圈的ID【翻页必传】
 |      :return: List数据
 |  
 |  get_moments_by_friend(self, wx_id, last_id=None)
 |      获取指定好友的朋友圈
 |      :param wx_id: 好友的微信ID
 |      :param last_id: 最后一条朋友圈的ID【翻页必传】
 |      :return: List数据
 |  
 |  get_mp_doc(self, gh_id, next_offset=None)
 |      获取公众号文章
 |      :param gh_id: 公众号ID
 |      :param next_offset: 下一页的偏移【翻页必传】
 |      :return: Dict数据
 |  
 |  get_self_info(self)
 |      获取个人信息
 |      :return: 未登录时返回None，登录成功返回字典数据
 |  
 |  get_small_app_code(self, app_id)
 |      获取小程序code
 |      :param app_id: 小程序的AppId
 |      :return: 小程序code
 |  
 |  hide_wx_windows(self)
 |      隐藏微信窗口
 |      :return: 无
 |  
 |  invite_friend_enter_chat_room(self, to_chat_room, to_wx_list)
 |      邀请好友进群
 |      :param to_chat_room: 群ID
 |      :param to_wx_list: 好友微信ID列表
 |      :return: 无
 |  
 |  like_moments(self, moments_id, state)
 |      朋友圈点赞/取消点赞
 |      :param moments_id: 朋友圈ID
 |      :param state: True:点赞 False:取消点赞
 |      :return: 无
 |  
 |  logout(self)
 |      退出登录
 |      :return: 无
 |  
 |  mask_msg_switch(self, to_id, switch)
 |      开启/关闭消息免打扰
 |      :param to_id: 好友ID/群ID
 |      :param switch: True:开启免打扰 False:关闭免打扰
 |      :return: 无
 |  
 |  moments_upload_img(self, path)
 |      朋友圈上传图片
 |      :param path: 图片的绝对路径
 |      :return: Dict数据
 |  
 |  ocr_recognition(self, path, is_split=False)
 |      OCR文字识别
 |      :param path: 图片的绝对路径
 |      :param is_split: 是否分段返回
 |      :return: 识别结果（分段模式返回list）
 |  
 |  pull_label_list(self)
 |      拉取标签列表
 |      :return: list数据
 |  
 |  pull_list(self, pull_type)
 |      拉取列表（好友/群/公众号/其他）
 |      :param pull_type: 好友:1 群:2 公众号:3 其他:4
 |      :return: list数据
 |  
 |  qr_code_join_chat_room(self, url)
 |      群二维码进群
 |      :param url: 群二维码解析的URL
 |      :return: 群ID
 |  
 |  query_friend_info(self, to_wx)
 |      查询好友信息
 |      :param to_wx: 要查询的微信ID
 |      :return: dict数据
 |  
 |  query_friend_info_by_net(self, to_wx)
 |      网络查询好友信息
 |      :param to_wx: 要查询的微信ID
 |      :return: dict数据
 |  
 |  query_wx_info_by_net(self, key)
 |      网络查询陌生人信息
 |      :param key: 手机号/QQ号/微信号
 |      :return: dict数据
 |  
 |  refund(self, msg_data)
 |      退款
 |      :param msg_data: 消息数据
 |      :return: 无
 |  
 |  save_img(self, save_path, msg_data)
 |      保存图片
 |      :param save_path: 保存图片的绝对路径
 |      :param msg_data: 消息数据
 |      :return: 无
 |  
 |  save_to_addr_book(self, to_chat_room, switch)
 |      群聊保存/取消保存到通讯录
 |      :param to_chat_room: 群ID
 |      :param switch: True:保存 False:取消保存
 |      :return: 无
 |  
 |  save_voice_switch(self, save_dir_path, switch)
 |      开启/关闭保存语音
 |      :param save_dir_path: 保存语音的绝对路径【目录路径】
 |      :param switch: True:开启 False:关闭
 |      :return: 无
 |  
 |  select_db(self, db_name, sql_text)
 |      查询数据库，注意，返字段取决于你的查询语句，查询结果较多可能会导致崩溃，建议运用好sql语句中的limit
 |      :param db_name: 数据库名称
 |      :param sql_text: sql语句
 |      :return: 查询结果【List数据】
 |  
 |  send_card_link(self, to_wx, title, desc, target_url, img_url)
 |      发送卡片链接
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param title: 卡片标题
 |      :param desc: 卡片描述
 |      :param target_url: 目标地址
 |      :param img_url: 卡片封面地址
 |      :return: 无
 |  
 |  send_card_link_moments(self, text, title, desc, target_url, thumb_url, is_private=False)
 |      发卡片链接朋友圈
 |      :param text: 文本内容
 |      :param title: 卡片标题
 |      :param desc: 卡片描述
 |      :param target_url: 目标地址
 |      :param thumb_url: 封面地址【上传接口返回的thumb_url】
 |      :param is_private: False:所有人可见 True:仅自己可见【默认为False】
 |      :return: 朋友圈ID
 |  
 |  send_file(self, to_wx, path)
 |      发送文件/视频消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param path: 文件/视频的绝对路径
 |      :return: 无
 |  
 |  send_friend_card(self, to_wx, friend_wx, friend_name)
 |      发送好友名片
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param friend_wx: 好友微信ID
 |      :param friend_name: 好友昵称
 |      :return: 无
 |  
 |  send_gif(self, to_wx, path)
 |      发送GIF表情
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param path: gif图片的绝对路径
 |      :return: 无
 |  
 |  send_img(self, to_wx, path)
 |      发送图片消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param path: 图片的绝对路径
 |      :return: 无
 |  
 |  send_img_text_moments(self, text, img_url_list=None, is_private=False)
 |      发图文朋友圈
 |      :param text: 文本内容
 |      :param img_url_list: 上传接口返回的图片url列表【不传则是发纯文本】
 |      :param is_private: False:所有人可见 True:仅自己可见【默认为False】
 |      :return: 朋友圈ID
 |  
 |  send_location(self, to_wx, lon, lat, address, detail_address)
 |      发送位置消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param lon: 经度
 |      :param lat: 纬度
 |      :param address: 地址
 |      :param detail_address: 详细地址
 |      :return: 无
 |  
 |  send_mp_card(self, to_wx, mp_id, mp_name)
 |      发送公众号名片
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param mp_id: 公众号ID
 |      :param mp_name: 公众号名称
 |      :return: 无
 |  
 |  send_notice(self, to_chat_room, content)
 |      发送群公告
 |      :param to_chat_room: 群ID
 |      :param content: 公告内容
 |      :return: 无
 |  
 |  send_or_forward_moments(self, xml_content, is_private=False)
 |      发送/转发朋友圈
 |      :param xml_content: xml内容
 |      :param is_private: False:所有人可见 True:仅自己可见【默认为False】
 |      :return: 朋友圈ID
 |  
 |  send_text(self, to_wx, msg)
 |      发送文本消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param msg: 消息内容
 |      :return: 无
 |  
 |  send_text_and_at_all(self, to_chat_room, msg)
 |      群聊发送文本信息并且@所有人
 |      :param to_chat_room: 群ID
 |      :param msg: 文本消息
 |      :return: 无
 |  
 |  send_text_and_at_member(self, to_chat_room, to_wx_list, msg, is_custom=False)
 |      群聊发送文本信息并且@指定群成员
 |      :param to_chat_room: 群ID
 |      :param to_wx_list: @人的微信ID列表
 |      :param msg: 文本消息
 |      :param is_custom: False:默认@位置 True:自行指定@位置【默认为False】
 |      :return: 无
 |  
 |  send_voice(self, to_wx, path, voice_time)
 |      发送语音消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param path: silk文件的绝对路径
 |      :param voice_time: 语音时长，单位:毫秒
 |      :return: True:成功 False:失败
 |  
 |  send_xml(self, to_wx, xml_str)
 |      发送XML消息
 |      :param to_wx: 接收者的微信ID/群ID
 |      :param xml_str: XML字符串
 |      :return: 无
 |  
 |  show_wx_windows(self)
 |      显示微信窗口
 |      :return: 无
 |  
 |  sns_download_img(self, url, md5, key, enc_idx, token, save_path)
 |      下载朋友圈图片
 |      :param url: 图片地址
 |      :param key: key
 |      :param md5: md5
 |      :param enc_idx: enc_idx
 |      :param token: token
 |      :param save_path: 保存路径
 |      :return: True:成功 False:失败
 |  
 |  sns_download_video(self, url, md5, key, save_path)
 |      下载朋友圈视频
 |      :param url: 视频地址
 |      :param key: key
 |      :param md5: md5
 |      :param save_path: 保存路径
 |      :return: True:成功 False:失败
 |  
 |  start_wx(self, path=None)
 |      启动微信，目前支持微信版本：V-3.9.10.19
 |      :param path: 保存登录二维码的绝对路径
 |      :return: (errno:状态码，errmsg:说明)
 |  
 |  top_chat_switch(self, to_id, switch)
 |      置顶/取消置顶聊天
 |      :param to_id: 好友ID/群ID
 |      :param switch: True:置顶 False:取消置顶
 |      :return: 无
 |  
 |  un_follow_mp(self, mp_id)
 |      取消关注公众号
 |      :param mp_id: 公众号ID
 |      :return: 无
 |  
 |  wx_search(self, keyword, next_offset=0, search_type=0, filter_sort=0, filter_type=0, filter_time=0, filter_scope=0)
 |      搜一搜
 |      :param keyword: 关键词
 |      :param next_offset: 下一页的偏移【翻页必传】
 |      :param search_type: 搜索类型
 |      :param filter_sort: 过滤-排序
 |      :param filter_type: 过滤-类型
 |      :param filter_time: 过滤-时间
 |      :param filter_scope: 过滤-范围
 |      :return: Dict数据
 |  
 |  ----------------------------------------------------------------------
```



## 声明

**本项目仅供技术研究，请勿用于非法用途，如有任何人凭此做何非法事情，均于作者无关，特此声明。**

