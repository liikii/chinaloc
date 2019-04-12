import requests
from pprint import pprint


haha = """Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 25
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _gscu_190942352=550411487otlpv90; _gscbrs_190942352=1; _gscs_190942352=t550568052fuk5r58|pv:1; JSESSIONID=1453910F3885196D4B931402AACC989B
Host: xzqh.mca.gov.cn
Origin: http://xzqh.mca.gov.cn
Pragma: no-cache
Referer: http://xzqh.mca.gov.cn/map
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
X-Requested-With: XMLHttpRequest"""


hd = dict()
for i, j in map(lambda s:s.split(':', 1), haha.splitlines()):
    hd[i.strip()] = j.strip()


# print(hd)
# pprint(hd)
# "shengji=黑龙江省(黑)"
u = 'http://xzqh.mca.gov.cn/selectJson'
dt = {'shengji': '黑龙江省(黑)'}
dt2 = {'shengji': '黑龙江省(黑)', 'diji': '佳木斯市'}

r = requests.post(u, data=dt2, headers=hd)
print(r.content.decode('utf8'))
