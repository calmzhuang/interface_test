from HTMLTestRunner_cn import HTMLTestRunner
from test_case.models.function import office365, new_report
import unittest
import time
import platform


def run():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/html/' + now + 'result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='自动化测试报告',
                                description='环境：{}  提醒：由于邮件中无法查看详细，建议查看附件中的测试报告！'.format('Mac' if platform.system() == 'Darwin' else platform.system()))
        discover = unittest.defaultTestLoader.discover('./test_case', pattern='*_sta.py')
        runner.run(discover)
    file_path = new_report('./report/html/')
    office365(file_path)


if __name__ == '__main__':
    run()
