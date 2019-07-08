# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# ProjectName:  interface_test
# Name:         function
# Description:  
# Author:       hanzhuang
# Date:         2019-07-01
# -------------------------------------------------------------------------------

from xlrd import open_workbook
from email.mime.text import MIMEText  # 专门发送正文
from email.mime.multipart import MIMEMultipart  # 发送多个部分
from email.mime.application import MIMEApplication  # 发送附件
from test_case.models.config import ConfigInit
import smtplib
import os


def get_interface_information(file_path):
    r_excel = open_workbook(file_path)
    table = r_excel.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    datas = []
    for i in range(nrows):
        row_datas = []
        for j in range(ncols):
            row_datas.append(str(table.cell(i, j).value).strip())
        datas.append(row_datas)
    row_head = datas[0]
    try:
        index_dict = {
            "url_index": row_head.index("url"),
            "method": row_head.index("method"),
            "data": row_head.index("data"),
            "header": row_head.index("header"),
            "status": row_head.index("status"),
            "condition": row_head.index("condition"),
            "except_result": row_head.index("except_result"),
            "is_login": row_head.index("is_login")
        }
        return index_dict, datas
    except Exception as e:
        print("请检查excel中的表头是否包含url、data、header、status、condition、except_result、is_login")
        print(e)
        exit()


# 获取case中参数的请求数据
def get_request_param(index_dict, datas):
    request_param = datas[index_dict.get("data")]
    request_param = eval(request_param)
    return request_param


# 获取case中参数的索引及case中的参数
def get_data(data_index):
    congfig_init = ConfigInit()
    index_dict, datas = get_interface_information(congfig_init.get_group_list_file_path)
    login_data = datas[1]
    datas = datas[data_index]
    request_param = get_request_param(index_dict, datas)
    return request_param, login_data, index_dict, datas


# 定义发送163邮件
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = "自动化测试报告"

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("calmzhuang@163.com", "password")
    smtp.sendmail("calmzhuang@163.com", "calmzhuang@163.com", msg.as_string())
    smtp.quit()
    print("email has sent out!")


# 定义发送outlook邮件
def office365(file_new):
    send_user = 'bjhl_test@outlook.com'  # 发件人
    password = 'password'  # 授权码/密码
    receive_users = ["bjhl_test@outlook.com", "hanzhuang@baijiahulian.com"]  # 收件人，可为list
    subject = '自动化测试报告'  # 邮件主题
    server_address = 'smtp.office365.com'  # 服务器地址

    # 构造一个邮件体：正文 附件
    msg = MIMEMultipart()
    msg['Subject'] = subject  # 主题

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 构建正文
    part_text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(part_text)  # 把正文加到邮件体里面去

    # 构建邮件附件
    # file = file           #获取文件路径
    part_attach1 = MIMEApplication(mail_body)  # 打开附件
    part_attach1.add_header('Content-Disposition', 'attachment', filename=file_new.split(os.path.sep)[-1])  # 为附件命名
    msg.attach(part_attach1)  # 添加附件

    # 发送邮件 SMTP
    try:
        smtp = smtplib.SMTP(server_address)  # 连接服务器，SMTP_SSL是安全传输
        smtp.ehlo()
        smtp.starttls()
        smtp.login(send_user, password)
        smtp.sendmail(send_user, receive_users, msg.as_string())  # 发送邮件
    except Exception as e:
        print("请到{}邮箱中进行账号验证".format(send_user))
        print(e)
    else:
        print('邮件发送成功！')


# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + fn))
    file_new = os.path.join(testreport, lists[-1])
    file_new = os.path.abspath('.') + file_new.strip('.')
    file_new = file_new.replace('/', os.path.sep)
    return file_new


