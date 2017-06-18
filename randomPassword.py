# coding=utf-8
import random

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
seed2 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sa = []

print ("1.只包含大小写字母")
print ("2.包含大小写字母与特殊符号")
passType = input("请选择密码类型(选择1 或 2)：")
length=input("请输入所需密码的位数： ")
if passType == 1:
    for i in range(length):
        sa.append(random.choice(seed2))
    salt = ''.join(sa)
    print salt
elif passType == 2:
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    print salt
else:
    print ("密码类型选择错误")
