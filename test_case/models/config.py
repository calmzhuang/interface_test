# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         common_interface_controller
# Description:
# Author:       hanzhuang
# Date:         2019-07-01
# -------------------------------------------------------------------------------
import os
# from fake_useragent import UserAgent

# 伪造请求头
# ua = UserAgent(use_cache_server=False, verify_ssl=False)

base_url = 'http://test-qun.umeng100.com/'


class ConfigInit(object):
    """
    初始化文件链接
    """
    def __init__(self):
        self.absolute_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.get_group_list_file_path = os.path.join(self.absolute_path, "basic_information", "get_group_list.xlsx")



