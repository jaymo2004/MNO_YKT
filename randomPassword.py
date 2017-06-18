# coding=utf-8
import random

setAll = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
setNumChar = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwordArray = []

print ("1.只包含大小写字母")
print ("2.包含大小写字母与特殊符号")
passType = input("请选择密码类型(选择1 或 2)：")
length=input("请输入所需密码的位数： ")
if passType == 1:
    for i in range(length):
        passwordArray.append(random.choice(setNumChar))
    salt = ''.join(passwordArray)
    print salt
elif passType == 2:
    for i in range(length):
        passwordArray.append(random.choice(setAll))
    salt = ''.join(passwordArray)
    print salt
else:
    print ("密码类型选择错误")
