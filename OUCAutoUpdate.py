import requests
import time
import os
from datetime import datetime, timezone, timedelta


tz = timezone(timedelta(hours=+8))
fmt = '%Y%m%d'
zoned_time = datetime.today().astimezone(tz)

Loginkey = os.environ["LOGINKEY"]
Sendkey = os.environ["SENDKEY"]
form_data = os.environ["FORM_DATA"]
form_data = form_data + '&date='+str(zoned_time.strftime(fmt))+'&created='+str(int(time.time()))

url = 'https://pingan.ouc.edu.cn/ncov/wap/default/save'

Cookies = {'eai-sess': Loginkey}

headers = {
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Referer':'https://pingan.ouc.edu.cn/ncov/wap/default/index',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
	}
try:
	r = requests.post(url,data = form_data,headers = headers,cookies = Cookies,verify=False)
except UnicodeEncodeError:
	r = requests.post(url,data = form_data.encode("utf-8"),headers = headers,cookies = Cookies,verify=False)

fturl = 'https://sctapi.ftqq.com/' + Sendkey + '.send?title= '+ str(r.json()["m"])

requests.get(fturl)
