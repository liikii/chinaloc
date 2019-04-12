import requests
import time
from pprint import pprint
from json import loads


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

hd = {'X-Requested-With': 'XMLHttpRequest', 'Connection': 'keep-alive',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
      'Cookie': '_gscu_190942352=550411487otlpv90; _gscbrs_190942352=1; _gscs_190942352=t550568052fuk5r58|pv:1; JSESSIONID=1453910F3885196D4B931402AACC989B',
      'Content-Length': '25', 'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Referer': 'http://xzqh.mca.gov.cn/map', 'Cache-Control': 'no-cache', 'Host': 'xzqh.mca.gov.cn',
      'Pragma': 'no-cache', 'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'http://xzqh.mca.gov.cn',
      'Accept-Language': 'en-US,en;q=0.9'}

# print(hd)

# with open('provinces.txt', encoding='utf8') as f:
#     print(f.read().splitlines())
prv = ['北京市(京)', '天津市(津)', '河北省(冀)', '山西省(晋)', '内蒙古自治区(内蒙古)', '辽宁省(辽)', '吉林省(吉)', '黑龙江省(黑)', '上海市(沪)', '江苏省(苏)', '浙江省(浙)', '安徽省(皖)', '福建省(闽)', '江西省(赣)', '山东省(鲁)', '河南省(豫)', '湖北省(鄂)', '湖南省(湘)', '广东省(粤)', '广西壮族自治区(桂)', '海南省(琼)', '重庆市(渝)', '四川省(川、蜀)', '贵州省(黔、贵)', '云南省(滇、云)', '西藏自治区(藏)', '陕西省(陕、秦)', '甘肃省(甘、陇)', '青海省(青)', '宁夏回族自治区(宁)', '新疆维吾尔自治区(新)', '香港特别行政区(港)', '澳门特别行政区(澳)', '台湾省(台)']


def get_city(ds):
    cts = []
    for d in ds:
        sjc = d['shengji']
        if sjc:
            cts.append(sjc)

        djc = d['diji']
        if djc:
            cts.append(djc)

        xjc = d['xianji']
        if xjc:
            cts.append(xjc)
    return cts


def print_all_city():
    # shengji diji xianji
    u = 'http://xzqh.mca.gov.cn/selectJson'
    for i in prv:
        dt = {'shengji': i}
        r = requests.post(u, data=dt, headers=hd, timeout=60)
        # print(r.content.decode('utf8'))
        d = loads(r.content.decode('utf8'))
        # print(d)
        # print("\t\t%s" % i.split('(', 1)[0])
        # print(','.join(get_city(d)))
        dj_city = get_city(d)
        for j in dj_city:
            dt2 = {'shengji': i, 'diji': j}
            r2 = requests.post(u, data=dt2, headers=hd, timeout=60)
            d2 = loads(r2.content.decode('utf8'))
            xj_cts = get_city(d2)
            print([i.split('(', 1)[0], j, xj_cts])
            time.sleep(1)
            # for k in xj_cts:
        print('-*-' * 100)
        time.sleep(1)


print_all_city()
