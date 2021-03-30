import datetime
import time



class UtilsDate(object):

    # 获取系统日期和时间
    @staticmethod
    def getCurrentDateAndTime():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # 获取系统日期
    @staticmethod
    def getCurrentDate():
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 获取系统时间
    @staticmethod
    def getCurrentTime():
        return time.strftime("%H:%M:%S", time.localtime(time.time()))

    # 获取时间戳
    @staticmethod
    def getTimeStamp():
        return (int(round(time.time() * 1000)))  # 毫秒级时间戳

    # 获取学号
    @staticmethod
    def getStudentId():
        return (int(round(time.time())))  #



    # 获取当前日期后几天
    @staticmethod
    def getOverTime(days):
        return (datetime.date.today() + datetime.timedelta(days=days)).strftime('%Y-%m-%d');


    def getTodayDate(self):
        nowdate=time.strftime("%Y-%m-%d",time.localtime(time.time()))
        return(nowdate)

    def getTodayTime(self):
        nowtime = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        return(nowtime)

    def getAppointedDate(self, appointedDate):  #参数是整数
        # 当前时间
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(days=appointedDate)
        # 获取想要的日期的时间
        #re_date = (today + offset).strftime('%Y-%m-%d %H:%M:%S')
        re_date = (today + offset).strftime('%Y-%m-%d')
        return re_date

if __name__ == '__main__':
    print("当前系统日期和时间："+UtilsDate.getCurrentDateAndTime())
    print("当前系统日期："+UtilsDate.getCurrentDate())
    print("当前系统时间："+UtilsDate.getCurrentTime())
    print("三天前的系统日期："+UtilsDate.getOverTime(-3))
    print(time.time() * 1000)
    print(round(time.time() * 1000))
    print("当前时间戳：" + str(UtilsDate.getTimeStamp1()))
    print(time.time())
    print(int(round(time.time() * 1000)))

