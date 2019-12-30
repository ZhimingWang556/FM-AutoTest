import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class TestCreateTimetable(unittest.TestCase):
    """创建时间表"""
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

    def test_ca_single_table(self):
        """创建00：00-24：00、发车间隔2分钟的时间表"""
        driver = self.driver
        # 点击新建按钮
        driver.find_element_by_class_name("btn-create").click()
        # 选择排班时间
        driver.find_element_by_xpath("//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange empty']").click()
        # 选择最近可用的第一个日期
        try:
            driver.find_element_by_xpath("//td[@class='available today']").click()
        except:
            element = driver.find_element_by_xpath("//td[@class='available'][1]")
            driver.execute_script('arguments[0].click()', element)
            driver.execute_script("arguments[0].click()", element)

        # 选择结束时间
        driver.find_element_by_xpath("//div[@class='el-date-editor mgll mgrl el-input el-input--prefix el-input--suffix el-date-editor--time-select']/input").click()
        element = driver.find_element_by_xpath("//div[@class='el-picker-panel time-select el-popper']/div/div/div/div[49]")
        driver.execute_script('arguments[0].click()', element)

        # 选择发车间隔
        driver.find_element_by_xpath("//div[@class='el-input el-input--suffix']/input").click()
        element = driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[3]")
        driver.execute_script('arguments[0].click()', element)

        # 点击完成编辑
        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        # 截图
        driver.save_screenshot("./reports/image/single_table.png")

    def test_cb_single_notask_table(self):
        """创建00：00-24：00、不发车的时间表"""
        driver = self.driver
        # 时间表首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[1]").click()

        # 点击新建按钮
        driver.find_element_by_class_name("btn-create").click()
        # 选择排班时间
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange empty']").click()
        # 选择最近可用的第一个日期
        element = driver.find_element_by_xpath("//td[@class='available'][1]")
        driver.execute_script('arguments[0].click()', element)
        driver.execute_script("arguments[0].click()", element)

        # 选择时间段的开始时间
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor mgrl el-input el-input--prefix el-input--suffix el-date-editor--time-select']/input").click()
        element = driver.find_element_by_xpath("//div[@class='el-scrollbar__view'][1]/div[1]")
        driver.execute_script('arguments[0].click()', element)

        # 选择结束时间
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor mgll mgrl el-input el-input--prefix el-input--suffix el-date-editor--time-select']/input").click()
        element = driver.find_element_by_xpath(
            "//div[@class='el-picker-panel time-select el-popper']/div/div/div/div[49]")
        driver.execute_script('arguments[0].click()', element)

        # 选择发车间隔【该时段不发车】
        driver.find_element_by_xpath("//div[@class='el-input el-input--suffix']/input").click()
        element = driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]")
        driver.execute_script('arguments[0].click()', element)

        # 点击完成编辑
        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        # 截图
        driver.save_screenshot("./reports/image/single_notask_table.png")

    def test_cc_double_table(self):
        """创建2个时间段、发车间隔2分钟的时间表"""
        '''
        创建两个时间段的时间表
        1、选择没有排班信息的非历史日期。
        2、选择多个时间段，2个
        3、选择最小发车间隔两分钟
        点击“完成创建”
        :return:
        '''
        driver = self.driver
        # 时间表首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[1]").click()

        # 点击新建按钮
        driver.find_element_by_class_name("btn-create").click()
        # 选择排班时间
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange empty']").click()
        # 选择最近可用的第一个日期
        element = driver.find_element_by_xpath("//td[@class='available'][1]")
        driver.execute_script('arguments[0].click()', element)
        driver.execute_script("arguments[0].click()", element)

        for i in range(2):
            xpath = []
            element_list = []
            # 结束时间
            xpath.append( "//ul[@class='c-period-list']/li[" + str((i+1)) + "]/div[2]")
            driver.find_element_by_xpath(xpath[0]).click()
            # 时间点
            xpath.append("/html/body/div["+ str((3+ 2*i))+"]/div[1]/div[1]/div/div[" + str(((i+1)*24+1)) + "]")
            element_list.append(driver.find_element_by_xpath(xpath[1]))
            driver.execute_script('arguments[0].click()', element_list[0])
            # 发车间隔
            xpath.append("//ul[@class='rule-list']/li[" + str((i+1)) + "]")
            driver.find_element_by_xpath(xpath[2]).click()
            # 15分钟发车间隔
            xpath.append("/html/body/div[" + str((4+2*i))+ "]/div[1]/div[1]/ul/li[2]")
            element_list.append(driver.find_element_by_xpath(xpath[3]))
            driver.execute_script('arguments[0].click()', element_list[1])
            xpath.clear()
            element_list.clear()

        # 点击完成编辑
        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        # 截图
        driver.save_screenshot("./reports/image/double_table.png")

    def test_cd_six_table(self):
        """创建6个时间段，最大发车间隔的时间表"""
        '''
        1、选择没有排班信息的非历史日期。
        2、选择多个时间段，6个
        3、选择最大发车间隔
        点击“完成创建”
        :return:
        '''

        driver = self.driver
        # 时间表首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[1]").click()

        # 点击新建按钮
        driver.find_element_by_class_name("btn-create").click()
        # 选择排班时间
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange empty']").click()
        # 选择最近可用的第一个日期
        element = driver.find_element_by_xpath("//td[@class='available'][1]")
        driver.execute_script('arguments[0].click()', element)
        driver.execute_script("arguments[0].click()", element)

        for i in range(6):
            xpath = []
            element_list = []
            # 结束时间
            xpath.append("//ul[@class='c-period-list']/li[" + str((i + 1)) + "]/div[2]")
            driver.find_element_by_xpath(xpath[0]).click()
            # 时间点
            xpath.append(
                "/html/body/div[" + str((3 + 2 * i)) + "]/div[1]/div[1]/div/div[" + str(((i + 1) * 8 + 1)) + "]")
            element_list.append(driver.find_element_by_xpath(xpath[1]))
            driver.execute_script('arguments[0].click()', element_list[0])
            # 发车间隔
            xpath.append("//ul[@class='rule-list']/li[" + str((i + 1)) + "]")
            driver.find_element_by_xpath(xpath[2]).click()
            # 15分钟发车间隔
            xpath.append("/html/body/div[" + str((4 + 2 * i)) + "]/div[1]/div[1]/ul/li[15]")
            element_list.append(driver.find_element_by_xpath(xpath[3]))
            driver.execute_script('arguments[0].click()', element_list[1])
            xpath.clear()
            element_list.clear()

        # 点击完成编辑
        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        # 截图
        driver.save_screenshot("./reports/image/six_table.png")

    def test_ce_most_table(self):
        """创建48个时间段，最大发车间隔的时间表"""
        '''
        1、选择没有排班信息的非历史日期。
        2、选择多个时间段，48个
        3、选择最大发车间隔
        点击“完成创建”
        :return:
        '''

        driver = self.driver
        # 时间表首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[1]").click()

        # 点击新建按钮
        driver.find_element_by_class_name("btn-create").click()
        # 选择排班时间
        driver.find_element_by_xpath(
            "//div[@class='el-date-editor el-range-editor el-input__inner el-date-editor--daterange empty']").click()
        # 选择最近可用的第一个日期
        element = driver.find_element_by_xpath("//td[@class='available'][1]")
        driver.execute_script('arguments[0].click()', element)
        driver.execute_script("arguments[0].click()", element)

        for i in range(48):
            xpath = []
            element_list = []
            # 结束时间
            xpath.append("//ul[@class='c-period-list']/li[" + str((i + 1)) + "]/div[2]")
            driver.find_element_by_xpath(xpath[0]).click()
            # 时间点
            xpath.append("/html/body/div[" + str((3 + 2 * i)) + "]/div[1]/div[1]/div/div[" + str((i + 2)) + "]")
            element_list.append(driver.find_element_by_xpath(xpath[1]))
            driver.execute_script('arguments[0].click()', element_list[0])
            # 发车间隔
            xpath.append("//ul[@class='rule-list']/li[" + str((i + 1)) + "]")
            driver.find_element_by_xpath(xpath[2]).click()
            # 15分钟发车间隔
            xpath.append("/html/body/div[" + str((4 + 2 * i)) + "]/div[1]/div[1]/ul/li[2]")
            element_list.append(driver.find_element_by_xpath(xpath[3]))
            driver.execute_script('arguments[0].click()', element_list[1])
            xpath.clear()
            element_list.clear()

        # 点击完成编辑
        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        # 截图
        driver.save_screenshot("./reports/image/most_table.png")