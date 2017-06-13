# coding=utf-8
import requests
import json
import hashlib
import time
t = time.time()


s = requests
headers = {
'Content-Type': 'application/json', 'charset=UTF-8'
'md5Sum': ''
}
key = ""
data = {"contentType":"1","MSISDN":"", "fromUrl":"2", "token":"", "smsContent":"你的消息是123456","requestId": ""}
data["requestId"]=int(t)
print data["requestId"]
m = hashlib.md5()
m.update(json.dumps(data) + key) # 需要将Json字符串先dump ，然后加上key一起做MD5运算
headers["md5Sum"] = m.hexdigest()
#print headers["md5Sum"] #检查MD5值
r = s.post('', json.dumps(data), headers=headers)
#print r.content
#print r.text
print r.status_code  #获取短信发送状态
if r.status_code == 200:
    print data["MSISDN"], "提醒短信发送成功"
