# -*- coding: UTF-8 -*-、
from PIL import Image
import pytesseract
from urllib import request
import time
import os

n=0
while n<1:
    n=n+1
    jpg_link='http://192.168.2.200:8081/verifycode'  #图片链接
    rq=time.strftime("%H-%M-%S",time.localtime())
    path=os.path.join(r'C:\Users\Administrator\Desktop\xiao\xiao',rq+'.png')#t图片保存路径及名称
    request.urlretrieve(jpg_link, path)#下载保存图片
    time.sleep(1)
time.sleep(3)

im=Image.open(r"C:\Users\Administrator\Desktop\xiao\xiao\test\test.png")
numlist=['0','1,','2','3','4','5','6','7','8','9']
num= pytesseract.image_to_string(im,lang='normal')#图片识别
print(num)
test=list(num)
list=[]
for i in test:
    if i in numlist:
        list.append(i)
print(list)
ls2=(str(j) for j in list)
ls3=''.join(ls2)
print(ls3)