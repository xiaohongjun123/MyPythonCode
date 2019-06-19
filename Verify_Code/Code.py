import chaojiying
from urllib import request
import time
import os
jpg_link="http://192.168.2.200:8081/verifycode"  #图片链接
rq=time.strftime("%H-%M-%S",time.localtime())
dir_path=os.path.dirname(os.path.abspath(__file__))
path=os.path.join(dir_path,rq+'.png')#t图片保存路径及名称
request.urlretrieve(jpg_link, path)#下载保存图片
time.sleep(1)
chaojiying = chaojiying.Chaojiying_Client('xhj123456', 'qazwsx123', '899485')	#用户中心>>软件ID 生成一个替换 96001
im = open(path, 'rb').read()
print (chaojiying.PostPic(im, 1902))
a=chaojiying.PostPic(im,1902)["pic_str"]

