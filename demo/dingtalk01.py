#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------- 
# @CreateTime   : 2020/2/20 21:45
# @Author       : WaterIce
# @Email        : waterice@vip.qq.com
# @Version      : 1.0 
# @File         : dingtalk01.py 
# @Desc         : 
# ------------------------------------

import logging
import time
import unittest
import config

from chatbot_help import DingtalkChatbot,is_not_null_and_blank_str, ActionCard, FeedLink, CardItem

__author__ = 'WaterIce'
__authorurl__ = 'https://zhiqiang.name'
logging.basicConfig(level=logging.ERROR)
global access_token,secret,webhookurl
class demo():
    def getconfig(self):
        global access_token, secret, webhookurl
        global_config = config.Config()
        # access_token
        access_token = global_config.getRaw('config', 'access_token')
        # secret
        secret = global_config.getRaw('config', 'secret')
        # webhookurl
        webhookurl = global_config.getRaw('config', 'webhookurl')
    def setUpClass(self):
        # 用户手机号列表
        self.at_mobiles = ['13990692500']
        # 初始化机器人
        self.ruixin = DingtalkChatbot(webhookurl+access_token,secret)
    def test_is_not_null_and_blank_str(self):
        """测试字符串不为空函数"""
        is_not_null_and_blank_str('')
        is_not_null_and_blank_str(' ')
        is_not_null_and_blank_str('   ')
        is_not_null_and_blank_str('abc')
        is_not_null_and_blank_str('123')
    def test_send_text(self):
        """测试发送文本消息函数"""
        self.ruixin.send_text(msg='我就是机器姬，机器姬就是我！', is_at_all=True)
        self.ruixin.send_text(msg='嘿我就是机器姬，机器姬就是我！', at_mobiles=self.at_mobiles)
        time.sleep(3)
    def test_send_image(self):
        """测试发送表情图片消息函数"""
        self.ruixin.send_image(pic_url='http://d.lanrentuku.com/down/png/1109/cute_boy/cute_boy_09.png')
        time.sleep(3)
    def test_send_link(self):
        """测试发送链接消息函数"""
        self.ruixin.send_link(title='万万没想到，机器姬竟然...', text='故事是这样子的...',
                                       message_url=__authorurl__,
                                       pic_url='http://d.lanrentuku.com/down/png/1109/cute_boy/cute_boy_12.png')

        time.sleep(3)
    def test_send_markdown(self):
        """测试发送Markdown格式消息函数"""
        # 1、提醒所有人
        self.ruixin.send_markdown(title='氧气文字', text='#### 成都天气\n'
                                                              '> 9度，西北风1级，相对温度73%，其实都是瞎猜的。\n\n'
                                                              '> ![美景](https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg)\n'
                                                              '> ###### 10点20分发布 [天气](' + __authorurl__ + ') \n',
                                           is_at_all=True)

        time.sleep(3)
        # 2、提醒指定手机用户，需要在text参数中@用户
        self.ruixin.send_markdown(title='氧气文字', text='#### 成都天气\n'
                                                              '> > 9度，西北风1级，相对温度73%，其实都是瞎猜的。\n\n'
                                                              '> ![美景](https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg)\n'
                                                              '> ###### 10点20分发布 [天气](' + __authorurl__ + ') \n',
                                           at_mobiles=self.at_mobiles)

        time.sleep(3)
    def test_send_actioncard(self):
        # 整体跳转ActionCard
        """测试发送整体跳转ActionCard消息功能（CardItem新API)"""
        btns1 = [CardItem(title="查看详情", url=__authorurl__)]
        actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jp) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
        self.ruixin.send_action_card(actioncard1)

        time.sleep(3)
        # 单独跳转ActionCard
        # 1、两个按钮选择
        """测试发送单独跳转ActionCard消息功能"""
        btns2 = [CardItem(title="支持", url=__authorurl__),
                 CardItem(title="反对", url=__authorurl__)]
        actioncard2 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg) \n### 故事是这样子的...',
                                 btns=btns2,
                                 btn_orientation=1,
                                 hide_avatar=1)
        self.ruixin.send_action_card(actioncard2)

        time.sleep(3)
        # 2、三个按钮选择
        btns3 = [CardItem(title="支持", url=__authorurl__),
                 CardItem(title="中立", url=__authorurl__),
                 CardItem(title="反对", url=__authorurl__)]
        actioncard3 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg) \n### 故事是这样子的...',
                                 btns=btns3,
                                 btn_orientation=1,
                                 hide_avatar=1)
        self.ruixin.send_action_card(actioncard3)

        time.sleep(3)
    def test_send_feedcard(self):
        """测试发送FeedCard类型消息功能（CardItem新API)"""
        # FeedCard类型
        card1 = CardItem(title="氧气美女", url=__authorurl__,
                         pic_url="https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg")
        card2 = CardItem(title="氧眼美女", url=__authorurl__,
                         pic_url="https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg")
        card3 = CardItem(title="氧神美女", url=__authorurl__,
                         pic_url="https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg")
        cards = [card1, card2, card3]
        self.ruixin.send_feed_card(cards)

        time.sleep(3)
    def test_send_feedcard_old_api(self):
        """测试发送FeedCard类型消息功能(FeedLink旧API)"""
        feedlink1 = FeedLink(title="氧气美女", message_url=__authorurl__,
                             pic_url="https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg")
        feedlink2 = FeedLink(title="氧眼美女", message_url=__authorurl__,
                             pic_url="https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg")
        feedlink3 = FeedLink(title="氧神美女", message_url=__authorurl__,
                             pic_url="https://img-arch.pconline.com.cn/images/upload/upc/tx/itbbs/1401/21/c26/30762046_1390298267194.jpg")
        links = [feedlink1, feedlink2, feedlink3]
        self.ruixin.send_feed_card(links)
        time.sleep(3)
def mini_sample():
    # *************************************这里填写自己钉钉群自定义机器人的token*****************************************
    webhook = webhookurl + access_token
    # 用户手机号列表
    at_mobiles = ['13990692500']
    # 初始化机器人
    ruixin = DingtalkChatbot(webhook)
    """测试发送文本消息函数"""
    ruixin.send_text(msg='我就是机器姬，机器姬就是我！', is_at_all=True)
    ruixin.send_text(msg='嘿我就是机器姬，机器姬就是我！', at_mobiles=at_mobiles)
    time.sleep(3)
if __name__ == '__main__':
    dem1=demo()
    dem1.getconfig()
    dem1.setUpClass()
    dem1.test_send_text()
    #dem1.test_send_image()
    #dem1.test_send_link()
    #dem1.test_send_markdown()
    #dem1.test_send_actioncard()
    #dem1.test_send_feedcard()
    #dem1.test_send_feedcard_old_api()

