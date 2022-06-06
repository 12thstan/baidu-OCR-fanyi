# 工程：OCR
# 创建时间：2022/6/2 10:08
# encoding:utf-8


import keyboard
import time
from PIL import ImageGrab
from aip import AipOcr


# 配置AipOcr
APP_ID =                                        # 你的 App ID
API_KEY =                                       # 你的 Api Key
SECRET_KEY =                                    # 你的 Secret Key

while True:
    # 截图
    keyboard.wait(hotkey='ctrl+c')          # 触发按键

    time.sleep(0.01)                        # 延迟

    # 保存图片
    image = ImageGrab.grabclipboard()
    image.save('OCR.png')                   # 图片命名为'OCR.png'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    # def get_file_content(filePath):
    #     with open('OCR.png', "rb") as fp:
    #         return fp.read()
    #
    # image = get_file_content('OCR.png')

    with open('OCR.png', "rb") as fp:
        image = fp.read()

        # 调用通用文字识别（标准版）
        res_image = client.basicGeneral(image)
        # print(res_image)

        # 筛选数据
        res = res_image['words_result']
        for i in res:
            print(i['words'])