# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         common_interface_controller
# Description:
# Author:       hanzhuang
# Date:         2019-07-01
# -------------------------------------------------------------------------------
import unittest
import json


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.response_time = None

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def response_assertion(self, index_dict, datas, response):
        self.assertEqual(int(eval(datas[index_dict.get("status")])), response.status_code)
        condition = datas[index_dict.get("condition")]
        expect_result = datas[index_dict.get("except_result")]
        if condition == "notRegexp":
            self.assertNotRegex(json.loads(response.content), expect_result)
        elif condition == "regexp":
            self.assertRegex(str(response.content), expect_result)


