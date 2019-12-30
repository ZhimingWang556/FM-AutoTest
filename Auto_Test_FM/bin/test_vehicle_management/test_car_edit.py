import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class TestEditTimetable(unittest.TestCase):
    """编辑排班车辆"""
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1440,754")
        url = "http://cp01-face-2.epc.baidu.com:8220/schedule/ondutycar"

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(300)
        self.driver.set_script_timeout(300)
        self.driver.get(url)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    def test_ec_editcar(self):
        """编辑排班车辆"""
        driver = self.driver
        # 点击编辑
        driver.find_element_by_xpath("//span[@class='el-checkbox__label']").click()
        # 取消选择第一个车辆
        driver.find_element_by_xpath("//label[@class='el-checkbox is-checked  selected']").click()
        # 点击确认修改
        driver.find_element_by_xpath("//button[@class='el-button submit-btn el-button--primary']").click()
        # 截图
        driver.save_screenshot("./reports/image/edit_car.png")