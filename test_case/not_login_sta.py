import unittest

from test_case.models import myunit
from test_case.page_obj.alarm_manage_controller import AlarmManage

class NotLoginTest(myunit.MyTest):
    '''
    未登录状态下，接口安全测试
    '''

    def test_not_login_batch_process(self):
        alarm_manage = AlarmManage()
        alarm_manage.r_session.cookies.clear()
        response = alarm_manage.batch_process(data='')
        self.assertEqual(response, '')

if __name__ == '__main__':
    unittest.main()
