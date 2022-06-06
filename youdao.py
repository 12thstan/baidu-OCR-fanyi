# 工程：youdao
# 创建时间：2022/6/1 21:41
# encoding:utf-8


import requests
import time
import random
import hashlib
import json


# 网址
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# 反爬
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1870252624@10.110.96.157; OUTFOX_SEARCH_USER_ID_NCOO=1338974472.751384; ___rl__test__cookies=1654489795853',
    'Referer': 'https://fanyi.youdao.com/'
}

# 时间戳   # lts
r = str(int(time.time()*1000))
# print(r)

# 随机数   # salt
random_num = random.randint(0,9)
i = r + str(random_num)
# print(i)

def data_new(e):

    # md5
    str_sign = "fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5"
    md5 = hashlib.md5()
    md5.update(str_sign.encode())
    sign = md5.hexdigest()
    # print(sign)

    # 添加参数      # post请求需要参数
    data_old = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': i,
        'sign': sign,
        'lts': r,
        'bv': 'dbf26599b4389c828cae8b896c9b0708',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return data_old

a = input("请输入需要翻译的内容：\n")
data = data_new(a)

# 请求
result = requests.post(url,headers=header,data=data).text
# print(result)

# 数据筛选
dict_res = json.loads(result)
print(dict_res['translateResult'][0][0]['tgt'])