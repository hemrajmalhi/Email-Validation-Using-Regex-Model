# Email validation in python (using regEx model)
# a-z
# 0-9
#  . _ time 1
#  @ time 1
# . 2,3
import re
email_codition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("enter the your email : ")

if re.search(email_codition,user_email):
    print("Right email ")
else:
    print("Wrong email ")

