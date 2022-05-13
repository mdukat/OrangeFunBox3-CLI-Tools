import requests
import json

url = 'http://192.168.1.1'
password = 'YOURPASSWORD'
ethData = '{"parameters":{"expression":{"eth":"((eth and edev) or (eth and ssw)) and .Active==true","wifi":"((wifi and edev) or (wifi and ssw)) and .Active==true"}}}'

with requests.Session() as s:
    r = s.post(url+'/authenticate?username=admin&password='+password)
    ctxID = json.loads(r.text)['data']['contextID']
    headers = {'X-Context': ctxID}
    r = s.post(url+'/sysbus/Devices:get', data=ethData, headers=headers)
    j = json.loads(r.text)
    print("PhysAddress        \tIPAddress\tName")
    for eth in j['status']['eth']:
        print(eth['PhysAddress'] + "\t" + eth['IPAddress'] + "\t" + eth['Name'])
    for wifi in j['status']['wifi']:
        print(wifi['PhysAddress'] + "\t" + wifi['IPAddress'] + "\t" + wifi['Name'])
