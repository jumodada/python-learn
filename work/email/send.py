# coding:utf-8

import time
import smtplib
import schedule  # pip install schedule

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


#第三方的smtp
mail_host = 'smtp.sina.com'
mail_user = 'conan868242'
mail_pass = 'cb997b01a87232b2'
# smtp 开通， 授权码

sender = 'conan868242@sina.com'
receivers = ['dewei.zhang@tusimple.com']

message = MIMEMultipart()

#message = MIMEText('<p style="color:red;">这是一个测试</p>', 'html', 'utf-8')

message['From'] = Header(sender)
message['Subject'] = Header('python脚本测试', 'utf-8')

attr = MIMEText(open('send.py', 'rb').read(), 'base64', 'utf-8')
attr['Content-Type'] = 'application/octet-stream'
attr['Content-Disposition'] = 'attachment;filename="send.py"'

message.attach(attr)
message.attach(MIMEText('这是一个带附件的邮件', 'plain', 'utf-8'))

def send():
    print('send start')
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host, 25)
        smtpobj.login(mail_user, mail_pass)
        smtpobj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException as e:
        print('error: %s' % e)


if __name__ == '__main__':
    schedule.every(10).seconds.do(send)
    

    while 1:
        schedule.run_pending()
        time.sleep(1)

