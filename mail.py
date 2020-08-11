#!/bin/bash/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''
Your Testing Job Failed.
'''
#the mail address and password section
my_address = 'your@gmail.com'
my_pass = '*********'
to_address = 'mailto@gmail.com'
#setting up mime
msg = MIMEMultipart()
msg['From'] = my_address
msg['To'] = to_address
msg['Subject'] = 'Testing status Failed'
#body and the attachments
msg.attach(MIMEText(mail_content, 'plain')) 
#create smtp sever for sending mail
sever = smtplib.SMTP('smtp.gmail.com', 587) 
sever.starttls()
sever.login(my_address, my_pass)
text = msg.as_string()
sever.sendmail(my_address, to_address, text)
sever.quit()
print('Mail sent Successfully')
