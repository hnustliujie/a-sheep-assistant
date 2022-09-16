# -*- coding: utf-8 -*-

"""
配置类
@author : lcry
@time : 2022/9/15 12:35
"""
import os

# 以下参数根据自己的需要进行修改：
SYS_CONFIG = {
    # 获取到的header中t值,必须修改为自己的
    "header_t": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ0MDUxMjMsIm5iZiI6MTY2MzMwMjkyMywiaWF0IjoxNjYzMzAxMTIzLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo0ODQ3NzA1OSwiZGVidWciOiIiLCJsYW5nIjoiIn0.8ekIN0THyXzKvItrzn6wprq0Lgw90EiX_ztWz7l2_QQ",
    # 获取到的header中的user-agent值
    "header_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN",
    # 设定的完成耗时，单位s，默认-1随机表示随机生成1s~1h之内的随机数，设置为正数则为固定
    "cost_time": 5,
    # 需要通关的次数，默认1
    "cycle_count": 1314
}


def get(key: str):
    value = os.getenv(key)
    if value is None:
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value
