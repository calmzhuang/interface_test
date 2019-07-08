# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         find_group_list
# Description:  
# Author:       hanzhuang
# Date:         2019-07-02
# -------------------------------------------------------------------------------

import unittest
import json

from test_case.models import myunit
from test_case.page_obj.common_interface_controller import CommonInterface
from test_case.models.function import get_data


class FindGroupList(myunit.MyTest):
    """
    获取群概况信息
    """

    # 已登录情况下，接口正常返回数据
    def test_get_group_list_only_login(self):
        request_param, login_data, index_dict, datas = get_data(2)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)

    # 未登陆情况下，接口无法返回数据
    def test_get_group_list_not_login(self):
        request_param, login_data, index_dict, datas = get_data(3)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)

    # 已登录情况下，关键词搜索
    def test_get_group_list_keyword_search(self):
        request_param, login_data, index_dict, datas = get_data(4)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)
        for data in json.loads(response.content).get("data"):
            self.assertRegex(data.get("name"), request_param.get("keyword"))

    # 已登录情况下，类别搜索
    def test_get_group_list_category_search(self):
        request_param, login_data, index_dict, datas = get_data(5)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)
        for data in json.loads(response.content).get("data"):
            self.assertEqual(int(request_param.get("id")), int(data.get("categoryId")))

    # 已登录情况下，非机器人群主查询
    def test_get_group_list_not_machine_search(self):
        request_param, login_data, index_dict, datas = get_data(6)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)
        for data in json.loads(response.content).get("data"):
            self.assertEqual(request_param.get("masterType"), data.get("masterType"))

    # 已登录情况下，机器人群主查询
    def test_get_group_list_machine_search(self):
        request_param, login_data, index_dict, datas = get_data(7)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)
        for data in json.loads(response.content).get("data"):
            self.assertEqual(3, data.get("masterType"), msg="返回数据的群主类型不是机器人")

    # 已登录情况下，查看可用群
    def test_get_group_list_view_available(self):
        request_param, login_data, index_dict, datas = get_data(8)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)

    # 已登录情况下，关键词搜索+类别搜索+机器人群主
    def test_get_group_keyword_category_machine_search(self):
        request_param, login_data, index_dict, datas = get_data(9)
        common_interface = CommonInterface()
        response_time, response = common_interface.interface_process(index_dict, login_data, datas)
        self.response_time = response_time
        self.response_assertion(index_dict, datas, response)
        for data in json.loads(response.content).get("data"):
            self.assertRegex(data.get("name"), request_param.get("keyword"))
            self.assertEqual(int(request_param.get("id")), int(data.get("categoryId")))
            self.assertEqual(0, data.get("masterType"))


if __name__ == '__main__':
    unittest.main(warnings='ignore')
