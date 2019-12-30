import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class TestEditTimetable(unittest.TestCase):
    """编辑时间表"""
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1440,754")
        url = "http://cp01-face-2.epc.baidu.com:8220/schedule/timetable"

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(300)
        self.driver.set_script_timeout(300)
        self.driver.get(url)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    def test_ea_edst(self):
        """编辑时间表"""
        driver = self.driver
        # 进入编辑后，点击历史任务，确认离开
        driver.find_element_by_xpath("//button[@class='el-button edit el-button--default is-plain']").click()
        driver.find_element_by_xpath("//div[@class='el-date-editor mgll mgrl el-input el-input--prefix el-input--suffix el-date-editor--time-select']").click()
        element = driver.find_element_by_xpath("//div[@class='el-scrollbar__view']/div[49]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath("//li[@class='el-menu-item'][3]").click()
        driver.save_screenshot("./test_case/images/history_in_edit.png")

        driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary ']").click()
        sleep(2)

        # 进入编辑后，点击历史任务，取消离开
        driver.get("http://cp01-face-2.epc.baidu.com:8220/schedule/timetable")
        driver.find_element_by_xpath("//button[@class='el-button edit el-button--default is-plain']").click()
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor mgll mgrl el-input el-input--prefix el-input--suffix el-date-editor--time-select']").click()
        element = driver.find_element_by_xpath("//div[@class='el-scrollbar__view']/div[49]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath("//li[@class='el-menu-item'][3]").click()
        driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small is-plain']").click()
        driver.save_screenshot("./test_case/images/cancel_history.png")

        # 点击取消编辑,并确定
        element = driver.find_element_by_xpath("//button[@class='el-button mgrl cancel-btn el-button--primary is-plain']")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary ']").click()
        driver.save_screenshot("./test_case/images/cancel_edit_confirm.png")

        # 编辑后点击取消编辑，并取消
        driver.find_element_by_xpath("//button[@class='el-button edit el-button--default is-plain']").click()
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor mgll mgrl el-input el-input--prefix el-input--suffix el-date-editor--time-select']").click()
        element = driver.find_element_by_xpath("//div[@class='el-scrollbar__view']/div[49]")
        driver.execute_script('arguments[0].click()', element)
        element = driver.find_element_by_xpath(
            "//button[@class='el-button mgrl cancel-btn el-button--primary is-plain']")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "//button[@class='el-button el-button--default el-button--small is-plain']").click()
        driver.save_screenshot("./test_case/images/cancel_edit_cancel.png")

        # 完成编辑
        element = driver.find_element_by_xpath("//button[@class='el-button mgll next-btn el-button--primary']")
        driver.execute_script('arguments[0].click()', element)
        sleep(1)
        driver.save_screenshot("./reports/image/edit_timetable.png")