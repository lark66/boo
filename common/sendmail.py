import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  email.message import EmailMessage
import imaplib


sender = '13693653825@163.com'
receiver = '348959820@qq.com'
smtpserver = 'smtp.163.com'
username = '13693653825@163.com'
password = '7777770kk'
mail_title = '主题：后台接口测试报告'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

# 邮件正文内容
#message.attach(MIMEText('的正文', 'plain', 'utf-8'))
#e_msg =EmailMessage()

pureText = MIMEText(open('9878.html', 'rb').read(), 'html', 'utf-8')
# 随便找的html文件，后面两个参数是告诉程序以html格式和utf-8字符
message.attach(pureText)

# 构造附件1（附件为TXT格式的文本）
#att1 = MIMEText(open('token检测.html', 'rb').read(), 'base64', 'utf-8')
#att1["Content-Type"] = 'html'
#att1["Content-Disposition"] = 'attachment; filename="9878"'
#message.attach(att1)



smtpObj = smtplib.SMTP_SSL('smtp.163.com',465)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法

smtpObj.login(username, password)
smtpObj.sendmail(sender, receiver, message.as_string())
print("邮件发送成功！！！")
smtpObj.quit()