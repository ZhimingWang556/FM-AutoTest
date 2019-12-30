import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestPageTurning(unittest.TestCase):
    """页面跳转"""
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1440,754")
        url = "http://cp01-face-2.epc.baidu.com:8220/schedule/group"

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(300)
        self.driver.set_script_timeout(300)
        self.driver.get(url)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    def test_page_turning(self):
        """验证界面跳转"""
        driver = self.driver
        # 时间表
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[1]").click()
        try:
            # 获取当前页面url并断言
            currentPageUrl = driver.current_url
            assert currentPageUrl == "http://cp01-face-2.epc.baidu.com:8220/schedule/timetable", "时间表网页网址非预期！"
        except Exception as e:
            print(e)
        # 安全员表
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[2]").click()
        try:
            # 获取当前页面url并断言
            currentPageUrl = driver.current_url
            assert currentPageUrl == "http://cp01-face-2.epc.baidu.com:8220/schedule/group", "安全员表网页网址非预期！"
        except Exception as e:
            print(e)
        # 任务分配
        driver.find_element_by_xpath("//li[@class='task el-submenu is-opened']/ul/li/ul/li[1]").click()
        try:
            # 获取当前页面url并断言
            currentPageUrl = driver.current_url
            assert currentPageUrl == "http://cp01-face-2.epc.baidu.com:8220/task/unallocated", "任务分配网页网址非预期！"
        except Exception as e:
            print(e)
        # 任务监控
        driver.find_element_by_xpath("//li[@class='task el-submenu is-active is-opened']/ul/li/ul/li[2]").click()
        try:
            # 获取当前页面url并断言
            currentPageUrl = driver.current_url
            assert currentPageUrl == "http://cp01-face-2.epc.baidu.com:8220/task/monitor", "任务监控网页网址非预期！"
        except Exception as e:
            print(e)
        # 历史任务
        driver.find_element_by_xpath("//li[@class='task el-submenu is-active is-opened']/ul/li/ul/li[3]").click()
        try:
            # 获取当前页面url并断言
            currentPageUrl = driver.current_url
            assert currentPageUrl == "http://cp01-face-2.epc.baidu.com:8220/task/allocated", "历史任务网页网址非预期！"
        except Exception as e:
            print(e)
        # 值班车辆
        driver.find_element_by_xpath("//li[@class='car el-submenu is-opened']/ul/li/ul/li").click()
        try:
            # 获取当前页面url并断言
            currentPageUrl = driver.current_url
            assert currentPageUrl == "http://cp01-face-2.epc.baidu.com:8220/schedule/ondutyCar", "值班车辆网页网址非预期！"
        except Exception as e:
            print(e)