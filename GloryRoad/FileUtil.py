import os
from DateUtil import currentDate,currentTime

def creatDir():
    currentPath=os.path.dirname(os.path.abspath(__file__))
    today=currentDate()
    dateDir=os.path.join(currentPath,today)
    print(dateDir)
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    now=currentTime()
    timeDir=os.path.join(dateDir,now)
    print(timeDir)
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir
print(creatDir())



