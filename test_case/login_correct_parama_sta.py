import unittest

from test_case.models import myunit
from test_case.page_obj.alarm_manage_controller import AlarmManage


class LoginCorrectParama(myunit.MyTest):
    '''
    已登录且参数正确状态下，接口正确响应测试
    '''

    def test_login_correct_parama(self):
        alarm_manage = AlarmManage()
        response = alarm_manage.batch_process(data='')
        self.assertEqual(response, '')


if __name__ == '__main__':
    unittest.main()