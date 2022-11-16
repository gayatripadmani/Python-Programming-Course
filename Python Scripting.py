## Python Scripting ##

# Scripting #

# Scripting in writing program to automated task and python write it self as scripting langauge

# OS Library stands for Operating Sysytem #

# import os
#
# def current_dir():
#     cwd = os.getcwd()
#     print(cwd)
#
# def file_path(filename):
#     path = os.path.abspath(filename)
#     print(path)
#
# current_dir()
# filename = "sample.txt"
# file_path(filename)

# Time Module #

# import time
#
# epc = time.time()
# print(epc)
#
# localtime = time.localtime(epc)
# print(localtime)
#
# print(localtime.tm_year)
#
# print(time.ctime(epc))

# SMTP Module -- This is protocol for sending E-mails #

# import smtplib
#
# sender_mail = 'padmanigayatri@gmail.com'
# receivers_mail = ['padmanigayatri167@gmail.com']
# message = """From: Gayatri %s
# To: Gayatri167 %s
# Subject: Sending SMTP e-mail
# This is a test e-mail message.
# """%(sender_mail,receivers_mail)
#
# try:
#    password = input('Enter the password: ');
#    smtpObj = smtplib.SMTP('gmail.com',587)
#    smtpObj.login(sender_mail,password)
#    smtpObj.sendmail(sender_mail, receivers_mail, message)
#    print("Successfully sent email")
# except Exception:
#    print("Error: unable to send email")

# import smtplib
#
# sender_mail = 'padmanigayatri@gmail.com'
# receivers_mail = ['padmanigayatri167@gmail.com']
# message = """From: Gayatri %s
# To: Gayatri167 %s
# Subject: Sending SMTP e-mail
# This is a test e-mail message.
# """%(sender_mail,receivers_mail)
#
# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender_mail, receivers_mail, message)
#    print("Successfully sent email")
#
# except Exception:
#    print("Error: unable to send email")

