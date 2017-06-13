# coding=utf-8
import requests
import json
import threading
import xlrd
import time
s = requests
def chaxun1():
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    queny = {"transactionId": "[CSP]-[QueryBalance]-[20170314150500]", "currentTime": "2017-04-06T15:05:00.020+0800",
             "purpose": "QueryBalance", "who": "CSP",
             "data": {"vin": "null", "ownerId": "null", "msisdn": "", "custom": "null"}}
    prefix = "861452769"
    data = xlrd.open_workbook('zjyktkj0425.xls')
    table = data.sheets()[0]
    x = table.row_values(1)
    nrows = table.nrows
    print "一共有"+str(nrows)+"个号码"
    #str(int(x[0]))
    for i in range(1,nrows,1):
        x = table.row_values(i)
        number =x[0]
        queny["data"]["msisdn"] = str(int(number))
        #print queny["data"]["msisdn"]
        jsonresult = s.post('', json.dumps(queny))
        balanceresult = (json.loads(jsonresult.text))
        try:
            if (balanceresult["data"]["detail"][0]["usedDataVolume"]):
                print queny["data"]["msisdn"], str(int(balanceresult["data"]["detail"][0]["usedDataVolume"])/1024)+"MB"
                if (int(balanceresult["data"]["detail"][0]["usedDataVolume"])/1024 >= 1024):
                    print queny["data"]["msisdn"] + "********请注意该用户已经超过阈值"
        except:
            continue
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())




threads = []
t1 = threading.Thread(target=chaxun1())
threads.append(t1)
#t2 = threading.Thread(target=chaxun2())
#threads.append(t2)
#t3 = threading.Thread(target=chaxun3())
#threads.append(t3)
#t4 = threading.Thread(target=chaxun4())
#threads.append(t4)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
