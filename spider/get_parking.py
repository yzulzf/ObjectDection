import requests
import re
import os

from bs4 import BeautifulSoup
url='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%A3%B3%B5%CE%BB&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
myweb=requests.get(url).text
urls=re.findall(r'"objURL":"(.*?)"', myweb)
#print(urls)
#print(myweb)
my_image='d:/my_image_parking/'
if not os.path.isdir(my_image):
    os.mkdir(my_image)
index=1
for url in urls:
    print('this is url',url)

    try:
        res=requests.get(url)
        print(res.status_code)
        if str(res.status_code)[0]=='4':
            print("未成功下载！",url)

    #if str(res.status_code)
    except Exception as e:
        print("got it")
    finally:
        filename=os.path.join(my_image,str(index)+".jpg")
        with open(filename,'wb') as f:
            f.write(res.content)
            index=index+1
            print("this is %s pic"% index)

