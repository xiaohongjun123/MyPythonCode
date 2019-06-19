import time
from datetime import datetime
def currentDate():
    #date=time.localtime()
    today=time.strftime("%Y-%m-%d",time.localtime())
    #today=str(date.tm_year)+"-"+str(date.tm_mon)+"-"+str(date.tm_mday)
    return today
def currentTime():
    timestr=datetime.now()
    now=timestr.strftime("%H-%M-%S")
    return now
if __name__=="__main__":
    print(currentDate())
    print(currentTime())