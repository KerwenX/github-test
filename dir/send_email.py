import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "aston16@163.com"  # 用户名
mail_pass = "CYSWJZTAPYJNYAUI"  # 口令

sender = mail_user
sender_name = "admin"  # 显示名称
receiver = 'hello.and.world@qq.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱，列表 发送会报错

# 邮件内容
message = MIMEText("测试邮件", 'plain', 'utf-8')
message['From'] = "{0}<{1}>".format(sender_name ,sender)
message['To'] = receiver
message['Subject'] = Header("Nvidia", 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
    smtpObj.quit()
    smtpObj.close()
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)