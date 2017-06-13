# coding=utf-8
import requests
import json
s = requests
headers = {
'Content-Type': 'application/json','charset=UTF-8'
}
for i in range(1, 5, 1):

    data["iccId"] = prefix + "{:0>4d}".format(i)
    r = s.post('', json.dumps(data))
    #print r.status_code
#print r.headers['content-type']
#print r.encoding
    print r.text
    print data["iccId"], (json.loads(r.text))["data"]["phoneNumber"]

