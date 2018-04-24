#!/usr/bin/python
# -*- coding: utf-8
'''
爬取彩票机首页数据
1.得到Session会话对象
2.用BeautifulSoup4爬取页面数据
3.get下一页并爬取数据
...
'''
__Author__ = '汪思源'
__Vision__ = 0.1
__Date__ = '2018.4.24 16/47'

from LoginFulei import *
from FuleiHeader import *
from bs4 import BeautifulSoup
import io
import sys

class SpiderIndex(object):
    #唯一会话id
    login = LoginFulei()
    session = login.session
    soup = None

    def __init__(self):
        global soup
        soup = BeautifulSoup(self.getHtml(), "html.parser")
        if not SpiderIndex.login.isLogin():
            SpiderIndex.login.doLogin()

    def getHtml(self):
        header = FuleiHeader.getshjList()
        header.setdefault('Cookie','PHPSESSID=%s' % SpiderIndex.login.getCookie())
        htm = self.session.get(r"http://www.kadawo.com/fulei/index.php/equipment/shjList",headers = header,allow_redirects=False)
        return htm.text

    def writeContnet(self):
        table = soup.find("table")
        for tr in table.findAll('tr'):
            for th in tr.findAll('th'):
                with open(r"/fuleiContent.txt",'ab') as fth:
                    fth.write(th.getText().encode('utf-8'))
            for td in tr.findAll('td'):
                with open(r"/fuleiContent.txt", 'ab') as ftd:
                    ftd.write(td.getText().encode('utf-8'))

    def getNextPage(self):
        next_page_tag = soup.find(re.compile(r"<a href='(.*?)'>下一页</a>"))
        next_url = "http://www.kadawo.com%s" % next_page_tag
        print(next_page_tag)
        print(next_url)


if __name__ == '__main__':
    spiner = SpiderIndex()
    # spiner.getHtml()
    spiner.getNextPage()