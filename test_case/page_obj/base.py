# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         common_interface_controller
# Description:
# Author:       hanzhuang
# Date:         2019-07-01
# -------------------------------------------------------------------------------
import requests
from test_case.models.config import base_url


class InterfaceBase(object):
    """
    接口基础类，用于所有接口的继承
    """
    def __init__(self):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.r_session = requests.session()

    # 定义get接口请求
    def get(self, url, params, headers=None):
        response = self.r_session.get(url=url, params=params, headers=self.headers if headers is None else headers)
        return response

    # 定义post接口请求
    def post(self, url, data=None, headers=None):
        response = self.r_session.post(url=url, data=data, headers=self.headers if headers is None else headers)
        return response

    # 定义head接口请求
    def head(self, url, params, headers=None):
        response = self.r_session.head(url=url, params=params, headers=self.headers if headers is None else headers)
        return response

    # 定义put接口请求
    def put(self, url, params, headers=None):
        response = self.r_session.put(url=url, params=params, headers=self.headers if headers is None else headers)
        return response

    # 定义delete接口请求
    def delete(self, url, params, headers=None):
        response = self.r_session.delete(url=url, params=params, headers=self.headers if headers is None else headers)
        return response

    # 定义options接口请求
    def options(self, url, params, headers=None):
        response = self.r_session.options(url=url, params=params, headers=self.headers if headers is None else headers)
        return response

    # 定义patch接口请求
    def patch(self, url, params, headers=None):
        response = self.r_session.patch(url=url, params=params, headers=self.headers if headers is None else headers)
        return response