import unittest
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from util.transform_time import transform_time


class TestApportionTask(unittest.TestCase):
    """任务分配"""
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1440,754")
        url = "http://cp01-face-2.epc.baidu.com:8220/task/unallocated"

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(300)
        self.driver.set_script_timeout(300)
        self.driver.get(url)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    def test_task_list(self):
        """检查分配列表中的任务是否符合发车前3小时后4.5分钟"""
        driver = self.driver
        # 获取列表中第一个任务的发车时间
        now_time = int(time.time())
        time_first = driver.find_element_by_xpath("//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr[1]/td[5]/div").get_attribute("innerHTML")
        # 转换成时间戳
        time_first = transform_time(time_first)
        # 当前时间与第一个任务发车时间的时间差
        time_first_interval = now_time - time_first
        self.assertLessEqual(time_first_interval, 270, msg="超过发车时间4.5分钟的任务仍然存在于分配列表中")
        # 获取最后一个任务的发车时间
        time_last = driver.find_element_by_xpath("//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr[last()]/td[5]/div").get_attribute("innerHTML")
        time_last = transform_time(time_last)
        # 当前时间与最后一个任务发车时间的时间差
        time_last_interval = time_last - now_time
        self.assertLessEqual(time_last_interval, 10800, msg="发车时间点前3小时的任务进入分配列表中")
        print(time_last_interval)

    def test_task_cancel(self):
        """取消某个任务"""
        driver = self.driver
        # 获取任务号
        task_id_qx = driver.find_element_by_xpath("//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr[3]/td[2]/div").get_attribute("innerHTML")
        print(task_id_qx)
        # 点击取消该任务
        driver.find_element_by_xpath("//div[@class='el-table__fixed-right']/div[2]/table/tbody/tr[3]/td[13]/div/div/button[2]").click()
        # 在弹出框选择取消原因
        driver.find_element_by_xpath("//div[@class='el-form-item need is-required']").click()
        # 选择取消原因『安全员问题』
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[5]").click()
        # 截图
        driver.save_screenshot("./reports/image/安全员问题取消任务.png")
        # 点击确认
        driver.find_element_by_xpath("//div[@class='el-dialog']/div[3]/div/button[2]").click()
        # 获取所有的task_id
        sleep(10)
        # 截图
        driver.save_screenshot("./reports/image/确认取消.png")
        task_id = []
        # elements = driver.find_elements_by_xpath("//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr")
        elements = driver.find_elements_by_xpath("//div[@class='el-table el-table--fit el-table--scrollable-x el-table--enable-row-transition']/div[3]/table/tbody/tr")
        print(len(elements))
        for i in range(len(elements)):
            xpath = "//div[@class='el-table__body-wrapper is-scrolling-left']/table/tbody/tr[" + str(i + 1) + "]/td[2]/div"
            id = driver.find_element_by_xpath(xpath).get_attribute("innerHTML")
            task_id.append(id)
        for j in range(len(elements)):
            self.assertNotEqual(task_id_qx, task_id[j], msg="任务取消后没有及时从任务列表清除")

    def test_modify_task(self):
        """修改任务"""
        driver = self.driver
        # 点击修改第三个任务
        driver.find_element_by_xpath(
            "//div[@class='el-table__fixed-right']/div[2]/table/tbody/tr[3]/td[13]/div/div/button[1]").click()
        # 点击修改分配车号
        driver.find_element_by_xpath(
            "//form[@class='el-form el-form--label-left']/div[3]/div").click()
        # 选择车号
        driver.find_element_by_xpath(
            "//body[@class='el-popup-parent--hidden']/div[3]/div[1]/div[1]/ul/li[1]").click()
        # 点击修改安全员
        driver.find_element_by_xpath(
            "//form[@class='el-form el-form--label-left']/div[4]/div").click()
        # 选择安全员
        driver.find_element_by_xpath(
            "//body[@class='el-popup-parent--hidden']/div[4]/div[1]/div[1]/ul/li[1]").click()
        # 截图
        driver.save_screenshot("./reports/image/modify_task.png")
        # 点击确认
        driver.find_element_by_xpath(
            "//body[@class='el-popup-parent--hidden']/div[1]/div[3]/div/div[3]/div/div/div[3]/div/button[2]").click()
        sleep(2)
        # 截图
        driver.save_screenshot("./reports/image/确认修改任务.png")