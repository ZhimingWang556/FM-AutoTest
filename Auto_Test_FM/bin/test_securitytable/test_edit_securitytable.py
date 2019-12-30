import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class TestEditSrcurityTable(unittest.TestCase):
    """编辑安全员"""
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

    def test_eb_edit_security(self):
        """编辑安全员"""
        driver = self.driver
        driver.find_element_by_xpath("//button[@class='el-button edit el-button--default is-plain']").click()
        # 选择安全员
        driver.find_element_by_xpath(
            "//div[@class='el-select__tags'][1]").click()
        # 取消第一个安全员
        element = driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "//span[@class='el-input__suffix-inner']/i").click()

        driver.find_element_by_xpath("//button[@class='el-button mgll btn el-button--primary is-plain']").click()
        driver.find_element_by_xpath(
            "//button[@class='el-button el-button--default el-button--small is-plain']").click()
        element = driver.find_element_by_xpath("//button[@class='el-button mgll btn el-button--primary']")
        driver.execute_script('arguments[0].click()', element)
        element = driver.find_element_by_xpath("//button[@class='el-button el-button--primary']")
        driver.execute_script('arguments[0].click()', element)

        driver.save_screenshot("./reports/image/edit_ecurity.png")