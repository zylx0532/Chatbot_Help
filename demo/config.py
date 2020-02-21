#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------- 
# @CreateTime   : 2020/2/21 0:10
# @Author       : WaterIce
# @Email        : waterice@vip.qq.com
# @Version      : 1.0 
# @File         : config.py 
# @Desc         : 
# ------------------------------------

import os
import configparser

class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            print("找不到%s尝试读取默认配置文件",config_file)
            config_file='configDemo.ini'
            self._path = os.path.join(os.getcwd(), config_file)
            if not os.path.exists(self._path):
                raise FileNotFoundError("找不到默认配置文件。退出")
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)