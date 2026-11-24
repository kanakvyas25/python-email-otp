import smtplib
import random
otp=random.randint(1111,9999)
sender='Email@gmail.com'
password='Password' 
reciver='Recivers Email'
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login(sender,password)
message=f'''
your otp is {otp}'''
server.sendmail(sender,reciver,message)
print("otp send succesfully...")
server.quit()