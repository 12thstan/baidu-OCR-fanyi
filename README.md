# baidu-OCR-fanyi
Python 日记 -- 百度 OCR 翻译

---

# 百度 OCR 翻译

<img src="https://npm.elemecdn.com/reverse-stu-allversions@1.0.14/img/2022.6.2-1.gif" width="800" />

**<p align = "center">效果展示</p>**

---

# 使用教程

- 打开 <code>new_OCR\dist\OCR.ini</code> 文件，把在 **准备工作** 获取的 <code>AppID</code> 、 <code>API Key</code> 和 <code>Secret Key</code> <font size="3" color="blue">对应填入</font> ， **运行exe文件** 即可
```ini
[aip]
APP_ID = 
API_KEY = 
SECRET_KEY = 
```

---

- <font size="3" color="red">如出现闪退</font> / <font size="3" color="blue">想换成自己的</font> , <font size="3" color="red">请</font> / <font size="3" color="blue">可</font> 更换以下内容
```ini
[config]
User-Agent = 

Cookie = 

bv = 
```

- 方法如下

1. **F12** 打开 **开发者工具** ，选择 **Network** ， 然后选择 **XHR**

2. 在 **翻译框** 输入任意 **文字** ，**页面** 会出现 **translate_** (如有多个选最新)

3. 点击 <font size="3" color="blue">translate_</font> ，在 <code>Headers</code> 页面可以找到 <code>User-Agent</code> 和 <code>Cookie</code> ,在 Payload 页面可以找到<code>bv</code> **<font size="3" color="red">(火狐浏览器的 <code>bv</code> 在请求页面)</font>**

4. 把找到的内容 **替换 ini 文件内容** ，**重新运行** 即可

5. 如不清楚文字描述可按 **如图 1 所示** 步骤 即可

<img src="https://npm.elemecdn.com/reverse-stu-allversions@1.0.15/img/2022.6.2-2.gif" width="700" />

<p align = "center">图 1</p>

---

# 补充
> github开源：https://github.com/12thstan/baidu-OCR-fanyi

> gitee开源：https://gitee.com/c12th/baidu-OCR-fanyi

> 原文：https://blog.c12th.cn/archives/7.html
