#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time

from bs4 import BeautifulSoup
from selenium import webdriver


a = [1,2]
b = [2, 3]
print a+b, a*2
exit()

opt = webdriver.ChromeOptions()          # 创建chrome对象
opt.add_argument('--no-sandbox')          # 启用非沙盒模式,linux必填,否则会报错:(unknown error: DevToolsActivePort file doesn't exist)......
opt.add_argument('--disable-gpu')          # 禁用gpu，linux部署需填，防止未知bug
# opt.add_argument('headless')          # 把chrome设置成wujie面模式，不论windows还是linux都可以，自动适配对应参数
driver = webdriver.Chrome(executable_path=r'chromedriver',options=opt)    # 指定chrome驱动程序位置和chrome选项
driver.get('https://youneed.win')          # 访问网页
time.sleep(6)           # 等待5秒
# driver.refresh()
content = driver.page_source          # 获取5秒后的页面
soup = BeautifulSoup(content,features='html.parser')    # 将获取到的内容转换成BeautifulSoup对象
driver.close()

print(soup.body.get_text())          # 通过BeautifulSoup对象访问获取到的页面内容