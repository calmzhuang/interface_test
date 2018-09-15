from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import win32com.client as win32
import smtplib
import unittest
import time
import os

# ===============定义发送邮件===============
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("username@163.com", "111111")
    smtp.sendmail("username@163.com", "calmzhuang@163.com", msg.as_string())
    smtp.quit()
    print("email has sent out!")

def send_outlook(file_new):
    olMailItem = 0
    obj = win32.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = "自动化测试报告"
    newMail.Body = "自动化测试已完成，详情见附件测试报告"
    newMail.To = "zhhan@niub.la"
    newMail.Attachments.Add(file_new)
    newMail.Send()
    print('email has sent out!')

# ===============查找测试报告目录，找到最新生成的测试报告文件===============
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

def run():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/html/' + now + 'result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='自动化测试报告',
                                description='环境：windows7  浏览器：Chrome')
        discover = unittest.defaultTestLoader.discover('./test_case', pattern='*_sta.py')
        runner.run(discover)
    file_path = new_report('./report/html/')
    file_path = os.path.abspath('.') + file_path.strip('.')
    file_path = file_path.replace('/', '\\')
    send_outlook(file_path)

if __name__ == '__main__':
    run()