#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019/02/15
@filename: get_pic_from_google.py
@author: sdhzdtwhm
Description:
    1.此脚本为使用selenium模拟访问爬取谷歌图片中的搜索结果
    2.运行环境为python3 需要安装selenium、bs4、requests库
    3.访问谷歌环境需要FQ
    4.需要下载谷歌浏览器的驱动
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup as bs
import uuid
import requests
import os


class Crawler:
    def __init__(self):
        self.url = base_url_part1 + search_query + base_url_part2

    """启动Chrome浏览器驱动"""
    def start_brower(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        """谷歌浏览器驱动地址"""
        executable_path = "D:\\google_driver\\chromedriver.exe"
        """启动Chrome浏览器"""
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
        """最大化窗口，因为每一次爬取只能看到视窗内的图片"""
        driver.maximize_window()
        """浏览器打开爬取页面"""
        driver.get(self.url)
        return driver

    def downloadImg(self, driver):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            'Connection': 'keep - alive',
            'content-type': 'application/json'
        }
        """滑动滚动条至：加载更多处"""
        for i in range(5):
            pos = i * 50000
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            time.sleep(3)
        print("准备点击：加载更多")
        driver.find_element_by_xpath("./*//input[@value='显示更多结果']").click()
        time.sleep(2)
        for i in range(5):
            pos = i * 50000
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            time.sleep(3)
        time.sleep(2)
        html_page = driver.page_source
        """利用Beautifulsoup4创建soup对象并进行页面解析"""
        soup = bs(html_page, "html.parser")
        """通过soup对象中的findAll函数图像信息提取"""
        imglist = soup.findAll('img', {'class': 'rg_ic rg_i'})
        url_list = []
        my_file=open('2.txt','a+')
        """获取图片地址，并添加进图片列表中"""
        for i in imglist:
            try:
                print(i['data-src'])
                my_file.write(i['data-src']+'\n')
                url_list.append(i['data-src'])
            except Exception as ex1:
                url_list.append(i['src'])
                #print('this sis ',i['src'])
                print(ex1)
        print("总共包含图片个数为：" + str(len(url_list)))
        #print('-----------------------------------------------', url_list[0])
        num=0
        for i in url_list:

            try:
                print('this is',i)
                ir = requests.get(i,headers=headers)
                #s_uuid = str(uuid.uuid1())
                #l_uuid = s_uuid.split('-')
               # name = ''.join(l_uuid)
                print("开始下载图片：%s.jpg" % str(num))
                open(localPath + '%s.jpg' % str(num), 'wb').write(ir.content)
                num=num+1
            except Exception as ex2:
                print('下载图片出错！！' + str(ex2))

    def run(self):
        driver = self.start_brower()
        self.downloadImg(driver)
        driver.close()
        print("Download has finished.")


if __name__ == '__main__':
    print(
        '\t\t\t**************************************\n\t\t\t**\t\tWelcome to Use Spider\t\t**\n\t\t\t*'
        '*************************************')
    """ base_url_part1以及base_url_part2都是固定不变的，无需更改"""
    base_url_part1 = 'https://www.google.com/search?q='
    base_url_part2 = '&source=lnms&tbm=isch'
    """爬取关键字"""
    search_list = ['parking spot']
    for search_query in search_list:
        localPath = 'D:/car/'
        try:
            os.mkdir(localPath)
        except Exception as e:
            print(e)
        craw = Crawler()
        craw.run()