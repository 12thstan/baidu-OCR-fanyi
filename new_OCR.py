# 工程：test
# 创建时间：2022/6/2 11:41
# encoding:utf-8


import keyboard
import time
import requests
import random
import hashlib
import json
import configparser
import pyperclip
import tkinter as tk
from PIL import ImageGrab
from aip import AipOcr


# 读取ini文件
aip = 'OCR.ini'
conf = configparser.ConfigParser()
conf.read(aip)

# 配置AipOcr
APP_ID = conf.get('aip', 'APP_ID')              # 你的 App ID
API_KEY = conf.get('aip', 'API_KEY')            # 你的 Api Key
SECRET_KEY = conf.get('aip', 'SECRET_KEY')      # 你的 Secret Key

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

while True:
    #   --------------- 截图识别 --------------
    # 截图
    keyboard.wait(hotkey='ctrl+c')      # 触发按键

    time.sleep(0.01)                    # 延迟

    # 保存图片
    image = ImageGrab.grabclipboard()
    image.save('OCR.png')               # 图片命名为'OCR.png'
    print('识别中...')

    with open('OCR.png', "rb") as fp:
        image = fp.read()

        # 调用通用文字识别（标准版）
        res_image = client.basicGeneral(image)
        # print(res_image)

        # 筛选数据
        all_text = ''
        res = res_image['words_result']
        for i in res:
            all_text += i['words'] + '\n'
        a = all_text
        print(a + '-' * 70)

    #   --------------- 有道翻译 --------------
    # 网址
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    # 反爬
    header = {
        'User-Agent': conf.get('config', 'User-Agent'),
        'Cookie': conf.get('config', 'Cookie'),
        'Referer': 'https://fanyi.youdao.com/'
    }

    # 时间戳
    r = str(int(time.time() * 1000))
    # print(r)

    # 随机数
    random_num = random.randint(0, 9)
    i = r + str(random_num)
    # print(i)


    def data_new(e):
        # md5
        str_sign = "fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5"
        md5 = hashlib.md5()
        md5.update(str_sign.encode())
        sign = md5.hexdigest()
        # print(sign)

        data_old = {
            'i': e,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': i,
            'sign': sign,
            'lts': r,
            'bv': conf.get('config', 'bv'),
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        return data_old

    data = data_new(a)

    # 请求
    result = requests.post(url, headers=header, data=data).text
    # print(result)

    # 数据筛选
    dict_res = json.loads(result)
    b = dict_res['translateResult'][0][0]['tgt']
    print(b + '\n')

    # copy
    pyperclip.copy(a + '\n' + b)
    time.sleep(0.02)
    # 弹窗
    root = tk.Tk()
    root.title("info")
    tk.Label(root, text="已复制", ).pack()       # 弹窗显示
    root.after(1000, lambda: root.destroy())    # 停留1s
    root.mainloop()
