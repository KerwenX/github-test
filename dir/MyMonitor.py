import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime

print("=====================Start Monitor ===================")

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "aston16@163.com"  # 用户名
mail_pass = "CYSWJZTAPYJNYAUI"  # 口令

sender = mail_user
sender_name = "aston"  # 显示名称 our service name
receiver = 'hello.and.world@qq.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱，列表 发送会报错

# 邮件内容
message = MIMEText("测试邮件", 'plain', 'utf-8')
message['From'] = "{0}<{1}>".format(sender_name, sender)
message['To'] = receiver
message['Subject'] = Header("Nvidia", 'utf-8')

last_send_time = datetime.datetime.now()

def send():
    global last_send_time
    current_time = datetime.datetime.now()
    delta = current_time - last_send_time
    # 如果两次发送邮件的间隔小于30分钟，就不发送
    if delta.seconds < 30*60:
        return
    print(datetime.datetime.now())
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
        # 发送邮件成功更新时间
        last_send_time = datetime.datetime.now()
        smtpObj.quit()
        smtpObj.close()
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)


while True:
    # 使用nvidia-smi命令获取显卡显存使用情况
    cmd = "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits"
    result = subprocess.check_output(cmd, shell=True).decode().strip().split('\n')

    # 解析结果
    gpu_memory_used = [int(x) for x in result]

    # 显示显卡显存使用情况
    for i, memory_used in enumerate(gpu_memory_used):
        print(f"{datetime.datetime.now()} : GPU {i}: Memory Used - {memory_used} MiB")

        # 可以在这里添加判断逻辑，根据显存使用情况执行相应的操作
        if memory_used < 4096:
            send()

    # 等待一段时间后继续监控
    time.sleep(60)  # 每10秒检查一次


# nohup python -u MyMonitor.py > log_file 2>&1 &
# 加上-u是为了让python的print快速输出