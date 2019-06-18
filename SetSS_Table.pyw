#coding:utf-8
import json
import requests
from bs4 import BeautifulSoup
import random
import os
from model import *
import time
from selenium import webdriver

fname = 'gui-config.json'

def main():
    url = "https://www.youneed.win/free-ss"
    print "if proxy error, set blue plane proxy off."
    killss()
    proxys = GetSS(url)
    r = random.randint(0,len(proxys)-1)
    print proxys[r]
    set_config(proxys[r])
    openss()


def GetSS(url, num=5):
    #get ss from free site. 
    # session = requests.Session()
    # session.trust_env = False       #no proxy
    # header = buildheader(url)
    # r = session.get(url, headers=header,verify=False)#5秒盾破不了
    # r = session.get(url, verify=False)
    # soup = BeautifulSoup(r.text, 'lxml')
    r = getsource(url)
    soup = BeautifulSoup(r, 'lxml')
    # print r.text
    section = soup.find('section', class_='context')
    Table = section.find('table')
    trs = Table.find_all('tr')
    proxys = []
    for tr in trs[1:num+1]: #get num  proxy.
        proxys.append( tr.text.split() )
    return proxys

def getsource(url):
    opt = webdriver.ChromeOptions()          # 创建chrome对象
    opt.add_argument('--no-sandbox')          # 启用非沙盒模式,linux必填,否则会报错:(unknown error: DevToolsActivePort file doesn't exist)......
    opt.add_argument('--disable-gpu')          # 禁用gpu，linux部署需填，防止未知bug
    # opt.add_argument('headless')          # 把chrome设置成wujie面模式，不论windows还是linux都可以，自动适配对应参数
    driver = webdriver.Chrome(executable_path=r'chromedriver',options=opt)    # 指定chrome驱动程序位置和chrome选项
    driver.get(url)          # 访问网页
    time.sleep(6)           # 等待5秒
    # driver.refresh()
    content = driver.page_source          # 获取5秒后的页面
    driver.close()
    return content
   

def buildheader(host):
    loc = host.find("://")
    if loc != -1:
        host = host[loc+3:]
    loc = host.find("/")
    if loc != -1:
        host = host[:loc]
    print host
    header = '''Host: %s
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8'''%host
    a = header.split('\n')
    ll = []
    for i in a:
        ll.append( i.split(': ', 1)[0:2] )
    # print ll
    return dict(ll)


def set_config(tuu):
    tuu = tuple(tuu[:4]*2)  #一号两配
    # print tuu
    dict_data = json.loads(model%tuu)
    f = open(fname, 'w')
    json.dump(dict_data, f, indent=2) #
    # f.write(model%tuu)  
    f.close()
    print('ok')

def killss():
    cmd = 'taskkill -f -im shadowsocks.exe'
    p = os.popen(cmd)
    print(p.read())

def openss():
    cmd = r'G:\Tools\ss\Shadowsocks.exe'
    p = os.popen(cmd)
    print(p.read())

if __name__ == '__main__':
    # a = [u'42.200.173.86', u'61551', u'7pSsOGjtHt', u'aes-256-cfb', u'11:12:16', u'HK']
    # set_config(a)
    # exit()
    main()

