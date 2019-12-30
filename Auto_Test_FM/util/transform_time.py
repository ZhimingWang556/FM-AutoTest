import datetime
import time


def transform_time(time1):
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    # 拼接年月日
    time_ori = year + "-" + month + "-" + day + " " + time1
    # 转换成时间数组
    timeArray = time.strptime(time_ori, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timStamp = int(time.mktime(timeArray))

    return timStamp