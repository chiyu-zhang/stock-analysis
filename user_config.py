#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
用户设置文件

作者：wking [http://wkings.net]
"""

# 配置部分开始
debug = False  # 是否开启调试日志输出  开=True  关=False

# 目录最好事先手动建立好，不然程序会出错
tdx = {
    'tdx_path': 'd:/software/tdx',  # 指定通达信目录
    'csv_lday': 'd:/software/tdx/data/lday_csv',  # 指定csv格式日线数据保存目录
    'pickle': 'd:/software/tdx/data/pickle',  # 指定pickle格式日线数据保存目录
    'csv_index': 'd:/software/tdx/data/index',  # 指定指数保存目录
    'csv_cw': 'd:/software/tdx/data/cw',  # 指定专业财务保存目录
    'csv_gbbq': 'd:/software/tdx/data/gbbq',  # 指定股本变迁保存目录
    'pytdx_ip': '123.125.108.24',  # 指定pytdx的通达信服务器IP
    'pytdx_port': 7709,  # 指定pytdx的通达信服务器端口。int类型
}

index_list = [  # 通达信需要转换的指数文件。通达信按998查看重要指数
    'sh999999.day',  # 上证指数
    'sh000300.day',  # 沪深300
    'sz399001.day',  # 深成指
]

# 配置部分结束
