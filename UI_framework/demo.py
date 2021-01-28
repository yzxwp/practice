from UI_framework.Logger import Logger
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from UI_framework.Logger import Logger


class YZXFrame(object):
    # 日志方法
    def logging(func):
        logger = Logger('yzxframe.log', level='debug').logger

        def wrapper(*args, **kwargs):
            if (args.__len__() > 1):
                logger.info(func.__name__ + ' 元素执行 ' + args[1])
            else:
                logger.info(func.__name__ + ' 已经执行 ')
            return func(*args, **kwargs)

        return wrapper

    @logging
    def __init__(self, driver):
        self.logger = Logger('yzxframe.log', level='debug').logger
        self.driver = driver

    @logging
    def open_browser(self, browser, url):
        try:
            if browser == "firefox":
                self.driver = webdriver.Firefox()
            elif browser == "chrome":
                self.driver = webdriver.Chrome()
            elif browser == "ie":
                self.driver = webdriver.Ie()
            self.driver.implicitly_wait(5)
            if url != None:
                try:
                    self.driver.get(url=url)
                except Exception:
                    self.logger.error("无效url地址")
            else:
                self.logger.error("url地址不能为空")
        except Exception:
            self.logger.error("不是使用firefox，chrome，ie三个浏览器")
            assert False
