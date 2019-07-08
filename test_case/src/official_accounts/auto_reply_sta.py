# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         auto_reply
# Description:  
# Author:       hanzhuang
# Date:         2019-07-01
# -------------------------------------------------------------------------------

import unittest

from test_case.models import myunit
from test_case.page_obj.common_interface_controller import CommonInterface
from test_case.models.function import get_interface_information


class AutoReplyPage(myunit.MyTest):
    '''
    已登录且参数正确状态下，接口正确响应测试
    '''

    # @staticmethod
    # def get_data():
    #     index_dict, datas = get_interface_information(get_group_list_file_path)
    #     return index_dict, datas
    #
    # def test_get_group_list(self):
    #     index_dict, datas = self.get_data()
    #     common_interface = CommonInterface()
    #     login_data = datas[1]
    #     datas = datas[2]
    #     response = common_interface.interface_process(index_dict, login_data, datas)
    #     self.response_assertion(index_dict, datas, response)


if __name__ == '__main__':
    unittest.main()