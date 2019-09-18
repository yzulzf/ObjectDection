import requests
from threading import Thread
import re
import time
import hashlib

class BaiDu_get:
    def __init__(self,name,page):
        self.start_time=time.time()
        self.name=name
        self.page=page
        #self.url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&rn=60&"
        #http: // image.baidu.com / search / flip?tn = baiduimage & ie = utf - 8 & word = car & rn = 60 & pn = 1
        self.url="https://image.baidu.com/search/flip?tn=baiduimage"

        self.num=0

    def queryset(self):
        pn=0
        for i in range(int(self.page)):
            pn += 60*i
            url=self.url+'&ie=utf-8'+'&word='+self.name+'&rn=60'+'&pn='+str(pn)
            #http: // image.baidu.com / search / flip?tn = baiduimage & ie = utf - 8 & word = ' car ' & pn = 60
           # print(url,name)
            #https://image.baidu.com/search/acjson&ie=utf-8&word=car&rn=60&pn=1
            #http: // image.baidu.com / search / flip?tn = baiduimage & ie = utf - 8 & word = % 27 % 20car % 20 % 27 & rn = 12 & pn = 3
            self.getrequest(url)

    def getrequest(self,url):
        print('[INFO]:开始发送请求'+url)
        ret=requests.get(url)
        if str(ret.status_code)=='200':
            print('[INFO]:request 200 ok:'+ret.url)
        else:
            print('[INFO]:request{},{}'.format(ret.status_code,ret.url))

        response=ret.content.decode()
        img_links=re.findall(r'thumbURL.*?\.jpg',response)
        allfile=open('1.txt','a+')

        links=[]
        for link in img_links:
            allfile.write(link+'\n')
            links.append(link[11:])

        self.thread(links)

    def saveimage(self,link):
        print('[INFO]:正在保存图片'+link)
        m=hashlib.md5()
        m.update(link.encode())
        name=m.hexdigest()
        ret=requests.get(link)
        image_content=ret.content
        filename=r'D:\\parking_test\\'+name+'.jpg'
        print(filename)

        with open(filename,'wb') as f:
            f.write(image_content)

        print('[INFO]:保存成功，图片名为{}.jpg'.format(name))


    def thread(self,links):
        self.num+=1
        for i,link in enumerate(links):
            print('*'*50)
            print(link)
            print('*'*50)
            if link:
                t=Thread(target=self.saveimage,args=(link,))
                t.start()
            self.num+=1
        print('一共进行了{}次请求'.format(self.num))
        self.now_del()
    def now_del(self):

        end_time=time.time()
        print('一共花了：{}'.format(end_time-self.start_time))

def main():
    name=input('请输入图片类型：')
    page=input('图片张数：')
    baidu=BaiDu_get(name,page)
    baidu.queryset()

if __name__ == '__main__':

    main()
#http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=car&pn=60
                              #flip?tn = baiduimage&ie=utf-8&word=car&rn=60&pn=1
#http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' car '&pn=60



