# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         common_interface_controller
# Description:  
# Author:       hanzhuang
# Date:         2019-07-01
# -------------------------------------------------------------------------------
import time
from test_case.page_obj.base import InterfaceBase


class CommonInterface(InterfaceBase):

    def interface_process(self, index_dict, login_datas, datas):
        login_url = self.base_url + login_datas[index_dict.get("url_index")]
        login_datas = login_datas[index_dict.get("data")]
        batch_process_url = self.base_url + datas[index_dict.get("url_index")]
        data = datas[index_dict.get("data")]
        headers = eval(datas[index_dict.get("header")])
        time_start = time.time()
        if datas[index_dict.get("is_login")] == 0:
            self.r_session.cookies.clear()
        else:
            self.post(url=login_url, data=login_datas, headers=headers)
        if datas[index_dict.get("method")] == 'post':
            if datas[index_dict.get("header")]:
                response = self.post(batch_process_url, data=data,
                                     headers=headers)
            else:
                response = self.post(batch_process_url, data=data)
        elif datas[index_dict.get("method")] == 'get':
            if datas[index_dict.get("header")]:
                response = self.get(batch_process_url, headers=headers)
            else:
                response = self.get(batch_process_url)
        else:
            response = ''
        time_end = time.time()
        response_time = time_end - time_start
        return response_time, response





