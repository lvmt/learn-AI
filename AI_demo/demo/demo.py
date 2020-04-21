#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""利用百度api实现语音识别
"""

# step1： pip install  baidu-aip -i https://pypi.douban.com/simple/ 

from aip import AipSpeech

API_ID = "17805504"
API_KEY = "oFuqUNS7EaHv7zDK5fnuhXti"
SECRET_KEY = "v0hpbqlvEGi81UT550HGDW1w4Sx7X12w"

client = AipSpeech(API_ID, API_KEY, SECRET_KEY)

# 中文： zh  粤语：ct  英文：en

result = client.synthesis('这是一个测试', 'zh', 1, {
    'vol': 20, 'per': 4
})

# 识别正确返回语音二进制； 识别错误反馈dict， 

if not isinstance(result, dict):
    with open('audio1.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)