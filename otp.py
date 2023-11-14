import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
    otp =  OTP + "  is your OTP"
    msg = otp

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("shydaparveen67@gmail.com","invm nnry bibo yxlb")
emailid = input("Please Enter your Email: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input("Please Enter your otp >>:")
if a == OTP:
    print("yes, your Otp is verified")
else:
    print("Please check your otp Again, Thank you!")1
