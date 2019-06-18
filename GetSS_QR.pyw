#coding:utf-8
import json
import requests
from bs4 import BeautifulSoup
import random
import os
import base64
from PIL import Image
import zbar
from model import *

fname = 'gui-config.json'
tempQR = "tempss.png"

def main():
    url = "https://ss.freess.org"
    # print "if proxy error, set blue plane proxy off."
    killss()
    pics = GetSSUrl(url)
    r = random.randint(0,len(pics)-1)
    savepic(pics[r])
    account = readQR()
    print account
    set_config(account)
    openss()


def GetSSUrl(url):
    #get ss from free site.
    # rescue_url = ["http://f55.fun", "http://55r.run"] 
    session = requests.Session()
    session.trust_env = False       #no proxy
    header = buildheader(url)
    r = session.get(url, headers=header,verify=False)
    # r = session.get(url, headers=header)
    ids = ["jp01", "jp02", "jp03", "us01", "us02", "us03"]
    pics = []
    # print url, r.text
    soup = BeautifulSoup(r.text, 'lxml')
    for idd in ids:
        a = soup.find("a", id=idd)
        pics.append( a['href'] )
    return pics

def buildheader(host):
    loc = host.find("://")
    if loc != -1:
        host = host[loc+3:]
    if host.endswith("/"):
        host = host[:-1]
    header = '''Host: %s
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: _ga=GA1.2.513400800.1531363158; _gid=GA1.2.1232985041.1536972498; _gat=1
If-None-Match: "2699-575dda7078543-gzip"
If-Modified-Since: Sat, 15 Sep 2018 00:02:14 GMT'''%host
    a = header.split('\n')
    ll = []
    for i in a:
        ll.append( i.split(': ', 1)[0:2] )
    # print ll
    return dict(ll)

def savepic(strs):
    #save base64code of QRcode to png.
    strs = strs.split(",",1)[1]
    try:
        imgdata=base64.b64decode(strs)
    except Exception as e:
        print "-%s-"%strs
        raise e
    file=open(tempQR,'wb')
    file.write(imgdata)
    file.close()

def readQR():
    #read ss account from QRcode picture, return account, delete pic.
    scanner = zbar.ImageScanner()
    scanner.parse_config("enable")
    pil = Image.open(tempQR).convert('L')
    width, height = pil.size
    raw = pil.tostring()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)
    data = ''
    for symbol in image:
        data+=symbol.data
    del(image)
    os.remove(tempQR)
    accounts = base64.b64decode(data[5:])
    # print accounts  #aes-256-cfb:f55.fun-73114797@jp01.1ss.bid:11425
    methodloc = accounts.find(":")
    locp = accounts.find("@")
    loclast = accounts.find(":", methodloc+1)
    method = accounts[0:methodloc]
    password = accounts[methodloc+1:locp]
    ip = accounts[locp+1:loclast]
    port = accounts[loclast+1:-1]
    return (ip, port, password, method)

def set_config(tuu):
    dict_data = json.loads(model%tuu)
    f = open(fname, 'w')
    json.dump(dict_data, f, indent=2)
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

    main()

