import unittest
from lib.HTMLTestRunner import HTMLTestRunner
import time



if __name__ == '__main__':
    # 定义测试用例的目录
    test_dir = './bin/'
    # test_dir = './bin/test_securitytable'
    # test_dir = './bin/test_vehicle_management'
    a = ["test_page_turning", "test_timetable", "test_securitytable", "test_vehicle_management", "test_task_association"]
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    fileName = "./reports/" + now + "result.html"
    # 生成HTML的测试报告
    fp = open(fileName, 'wb')
    for i in range(len(a)):
        print("%s" % (test_dir+a[i]))
        dis = unittest.TestLoader()
        suit = dis.discover(test_dir+a[i], pattern='test_*.py')
        runner = HTMLTestRunner(stream=fp,
                                title="FM排班表测试报告",
                                description="运行环境：MACos，Chrome浏览器"
                                )
        runner.run(suit)
    #suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # runner = HTMLTestRunner(stream=fp,
    #                         title="FM排班表测试报告",
    #                         description="运行环境：MACos，Chrome浏览器"
    #                         )
    # runner.run(suit)
    fp.close()