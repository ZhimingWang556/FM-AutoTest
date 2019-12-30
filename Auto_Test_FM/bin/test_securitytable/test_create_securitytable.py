import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCreateSecurityTable(unittest.TestCase):
    """创建安全员"""
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


    def test_cf_single_security(self):
        """创建单组、一个安全员、覆盖24小时的安全员表"""
        driver = self.driver
        # 点击新建按钮
        driver.find_element_by_xpath("//a[@class='btn-create']").click()

        # 排班时间
        driver.find_element_by_xpath("//div[@class='date']/div").click()
        try:
            driver.find_element_by_xpath("//td[@class='available today']").click()
        except:
            element_1 = driver.find_element_by_xpath("//td[@class='available'][1]")
            driver.execute_script('arguments[0].click()', element_1)
            driver.execute_script('arguments[0].click()', element_1)

        # 选择安全
        # 选择安全员
        xpath_1 = "//i[@class='el-select__caret el-input__icon el-icon-arrow-up'][1]"
        driver.find_element_by_xpath(xpath_1).click()
        for j in range(4):
            xpath_2 = "//ul[@class='el-scrollbar__view el-select-dropdown__list'][1]/li[" + str(
                j + 1) + "]"
            driver.find_element_by_xpath(xpath_2).click()
        xpath_3 = "//i[@class='el-select__caret el-input__icon el-icon-arrow-up is-reverse'][1]"
        driver.find_element_by_xpath(xpath_3).click()

        sleep(0.5)

        # 选择时间段
        # 开始时间
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[1]").click()

        # 结束时间
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[49]").click()

        # driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        driver.save_screenshot("./reports/image/single_4_24h_security.png")

    def test_cg_single_8h_security(self):
        """创建单组、一个安全员、00：00-8：00的安全员表"""
        driver = self.driver

        # 安全员首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[2]").click()

        # 点击新建按钮
        driver.find_element_by_xpath("//a[@class='btn-create']").click()

        # 排班时间
        driver.find_element_by_xpath("//div[@class='date']/div").click()
        element_1 = driver.find_element_by_xpath("//td[@class='available'][1]")
        driver.execute_script('arguments[0].click()', element_1)
        driver.execute_script('arguments[0].click()', element_1)

        # 选择安全
        driver.find_element_by_xpath("//i[@class='el-select__caret el-input__icon el-icon-arrow-up']").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]").click()
        driver.find_element_by_xpath(
            "//i[@class='el-select__caret el-input__icon el-icon-arrow-up is-reverse']").click()

        sleep(1)

        # 选择时间段
        # 开始时间
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[1]").click()

        # 结束时间
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[17]").click()

        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        driver.save_screenshot("./reports/image/single_security.png")

    def test_ch_single_most_security(self):
        """创建一组、所有安全员、时间间隔30分钟的安全员表"""
        # 起止日期选择多单天（正常输入）
        # 1、只选1组
        # 2、选择所有的安全员
        # 3、选择时间间隔30分钟
        # 点击“完成创建”
        driver = self.driver

        # 安全员首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[2]").click()

        # 点击新建按钮
        driver.find_element_by_xpath("//a[@class='btn-create']").click()

        # 排班时间
        driver.find_element_by_xpath("//div[@class='date']/div").click()
        element_1 = driver.find_element_by_xpath("//td[@class='available'][1]")
        element_2 = driver.find_element_by_xpath("//td[@class='available'][2]")
        driver.execute_script('arguments[0].click()', element_1)
        driver.execute_script('arguments[0].click()', element_2)

        # 选择安全员
        driver.find_element_by_xpath("//i[@class='el-select__caret el-input__icon el-icon-arrow-up']").click()
        for i in range(17):
            xpath = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[" + str(i + 1) + "]"
            driver.find_element_by_xpath(xpath).click()
        driver.find_element_by_xpath(
            "//i[@class='el-select__caret el-input__icon el-icon-arrow-up is-reverse']").click()

        sleep(0.5)

        # 选择时间段
        # 开始时间
        for j in range(48):
            # 开始时间
            xpath_1 = "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[" + str(
                j + 1) + "]/div[1]"
            driver.find_element_by_xpath(xpath_1).click()
            xpath_2 = "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[" + str(
                j + 1) + "]/div[1]/div/div[1]/div[1]/div/div[" + str(j + 1) + "]"
            element = driver.find_element_by_xpath(xpath_2)
            driver.execute_script('arguments[0].click()', element)
            # 结束时间
            xpath_3 = "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[" + str(
                j + 1) + "]/div[2]"
            driver.find_element_by_xpath(xpath_3).click()
            xpath_4 = "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[" + str(
                j + 1) + "]/div[2]/div/div[1]/div[1]/div/div[" + str(j + 2) + "]"
            element = driver.find_element_by_xpath(xpath_4)
            driver.execute_script('arguments[0].click()', element)
            if j == 0:
                driver.find_element_by_xpath("//i[@class='o-icon add ml48']").click()
            else:
                driver.find_element_by_xpath("//button[@class='period-btn'][2]/i").click()

        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        driver.save_screenshot("./reports/image/single_most_security.png")

    def test_ci_4G_4P_24H(self):
        """创建4组，每组4个安全员，四组时间有交集覆盖24小时的安全员表"""
        '''
        # 起止日期选择多单天（正常输入）
    # 1、选择4组
    # 2、每组4个安全员
    # 3、4组时间有交集，覆盖24小时
    # 点击“完成创建”
        :return:
        '''
        driver = self.driver
        # 安全员首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[2]").click()
        # 点击新建按钮
        driver.find_element_by_xpath("//a[@class='btn-create']").click()

        # 排班时间
        driver.find_element_by_xpath("//div[@class='date']/div").click()
        element_1 = driver.find_element_by_xpath("//td[@class='available'][1]")
        element_2 = driver.find_element_by_xpath("//td[@class='available'][2]")
        driver.execute_script('arguments[0].click()', element_1)
        driver.execute_script('arguments[0].click()', element_2)

        # 第一组
        # 选择安全员
        driver.find_element_by_xpath("//i[@class='el-select__caret el-input__icon el-icon-arrow-up']").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[3]").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[4]").click()
        driver.find_element_by_xpath(
            "//i[@class='el-select__caret el-input__icon el-icon-arrow-up is-reverse']").click()

        sleep(0.5)

        # 选择时间段
        # 开始时间
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[1]").click()

        # 结束时间
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[13]").click()

        # 增加组
        driver.find_element_by_xpath("//div[@class='groups-btn']").click()

        # 第二组
        # 选择安全员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[3]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/span/span/i").click()

        # 选择时间段
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[1]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[11]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[25]")
        driver.execute_script('arguments[0].click()', element)

        # 增加组
        driver.find_element_by_xpath("//div[@class='groups-btn']").click()

        # 第三组
        # 选择安全员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[3]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/span/span/i").click()

        # 选择时间段
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[1]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[23]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[37]")
        driver.execute_script('arguments[0].click()', element)

        # 增加组
        driver.find_element_by_xpath("//div[@class='groups-btn']").click()

        # 第四组
        # 选择安全员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[3]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[2]/span/span/i").click()

        # 选择时间段
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[1]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[35]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[49]")
        driver.execute_script('arguments[0].click()', element)

        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        driver.save_screenshot("./reports/image/4G_4P_security.png")

    def test_cj_4G_4P_nocross_not24H(self):
        """创建4组、每组4个安全员、四组时间无交集，不覆盖24小时的安全员表"""
        '''
        # 起止日期选择多单天（正常输入）
    # 1、选择4组
    # 2、每组4个安全员
    # 3、4组时间没有交集，不覆盖24小时
    # 点击“完成创建”
        :return:
        '''
        driver = self.driver
        # 安全员首页
        driver.find_element_by_xpath("//li[@class='schedule el-submenu is-active is-opened']/ul/li[2]").click()
        # 点击新建按钮
        driver.find_element_by_xpath("//a[@class='btn-create']").click()

        # 排班时间
        driver.find_element_by_xpath("//div[@class='date']/div").click()
        element_1 = driver.find_element_by_xpath("//td[@class='available'][1]")
        element_2 = driver.find_element_by_xpath("//td[@class='available'][2]")
        driver.execute_script('arguments[0].click()', element_1)
        driver.execute_script('arguments[0].click()', element_2)

        # 第一组
        # 选择安全员
        driver.find_element_by_xpath("//i[@class='el-select__caret el-input__icon el-icon-arrow-up']").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[2]").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[3]").click()
        driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[4]").click()
        driver.find_element_by_xpath(
            "//i[@class='el-select__caret el-input__icon el-icon-arrow-up is-reverse']").click()

        sleep(0.5)

        # 选择时间段
        # 开始时间
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[1]").click()

        # 结束时间
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[11]").click()

        # 增加组
        driver.find_element_by_xpath("//div[@class='groups-btn']").click()

        # 第二组
        # 选择安全员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[3]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][2]/div/div[1]/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/span/span/i").click()

        # 选择时间段
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[1]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[13]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[23]")
        driver.execute_script('arguments[0].click()', element)

        # 增加组
        driver.find_element_by_xpath("//div[@class='groups-btn']").click()

        # 第三组
        # 选择安全员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[3]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][3]/div/div[1]/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/span/span/i").click()

        # 选择时间段
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[1]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[25]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[35]")
        driver.execute_script('arguments[0].click()', element)

        # 增加组
        driver.find_element_by_xpath("//div[@class='groups-btn']").click()

        # 第四组
        # 选择安全员
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[3]").click()
        driver.find_element_by_xpath(
            "//div[@class='el-select-dropdown el-popper is-multiple is-fit'][4]/div/div[1]/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[2]/span/span/i").click()

        # 选择时间段
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[1]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[1]/div/div[1]/div[1]/div/div[37]")
        driver.execute_script('arguments[0].click()', element)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[2]").click()
        sleep(0.5)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/ul/li/div[2]/div/div[1]/div[1]/div/div[49]")
        driver.execute_script('arguments[0].click()', element)

        driver.find_element_by_xpath("//div[@class='opt']/button[2]").click()

        # 截图
        driver.save_screenshot("./reports/image/4G_4P_nocross_not24H_security.png")