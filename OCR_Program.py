# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:53:16 2026

@author: 爱丽丝
"""
# -*- coding: utf-8 -*-
from aip import AipOcr

# ===== 1. 填入你自己的三把钥匙 =====
APP_ID = '124759115'
API_KEY = 'U9Zcy9WOYRtQzH5qrTS4mMev'
SECRET_KEY = 'rHRWRAHbtVjs6993J7GuzK1NuN3epCCp'

# ===== 2. 初始化客户端对象 =====
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# ===== 3. 读取本地图片（二进制） =====
with open('Webpage_Screenshot.png', 'rb') as f:
    imagedata = f.read()

# ===== 4. 调用通用文字识别接口 =====
result = aipOcr.basicGeneral(imagedata)

# ===== 5. 打印原始返回信息 =====
print(result)

# ===== 6. 把识别出的文字写入 txt 文件 =====
if 'words_result' in result:
    with open('蓝桥杯大赛获奖情况.txt', 'w', encoding='utf-8') as file:
        for entry in result['words_result']:
            file.write(entry['words'] + '\n')
    print('识别成功，已写入 蓝桥杯大赛获奖情况.txt')
else:
    print('识别失败，返回内容：', result)
