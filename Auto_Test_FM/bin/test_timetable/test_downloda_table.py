import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class TestDownloadTable(unittest.TestCase):
    """下载时间表"""
    def setUp(self) -> None:
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

    def testdownloadtable(self):
        """下载时间表"""
        driver = self.driver
        driver.find_element_by_xpath("//button[@class='el-button download el-button--default is-plain']").click()
        element = driver.find_element_by_xpath("//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange']")
        driver.execute_script('arguments[0].click()', element)
        element = driver.find_element_by_xpath("//button[@class='el-button el-button--primary']")
        driver.execute_script('arguments[0].click()', element)


        driver.get("http://cp01-face-2.epc.baidu.com:8220/schedule/timetable")
        driver.find_element_by_xpath("//button[@class='el-button download el-button--default is-plain']").click()
        element = driver.find_element_by_xpath(
            "//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange']")
        driver.execute_script('arguments[0].click()', element)
        element = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[6]/td[3]")
        driver.execute_script('arguments[0].click()', element)
        element = driver.find_element_by_xpath(
            "/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[6]/td[4]")
        driver.execute_script('arguments[0].click()', element)
        element = driver.find_element_by_xpath("//button[@class='el-button el-button--primary']")
        driver.execute_script('arguments[0].click()', element)