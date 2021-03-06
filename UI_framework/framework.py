import os
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from UI_framework.Logger import Logger


class BlueRose(object):
    """
        对selenium框架的二次开发，更能体现
    """

    def logging(func):
        logger = Logger('blueRose.log', level='debug').logger

        def wrapper(*args, **kwargs):
            if (args.__len__() > 1):
                logger.info(func.__name__ + ' 执行 ' + args[1])
            else:
                logger.info(func.__name__ + ' 执行')
            return func(*args, **kwargs)

        return wrapper

    #
    def __init__(self, browser='firefox', isMultitask=False):
        self.logger = Logger('blueRose.log', level='debug').logger
        self.seconds = 30
        # 存储错误截图的列表
        self.imgs = []
        if isMultitask:
            self.initMultitaskDriver(browser, serverUrl='http://localhost:4444/wd/hub')
        else:
            self.initDriver(browser)

    def initDriver(self, browser='firefox', wait_time=5):
        """
        浏览器：默认为火狐浏览器，但是可以选择谷歌或者IE浏览器；
                打开浏览器的实践默认为5s，可修改；
                当输入的游览器不在"firefox""Firefox""chrome""Chrome""ie""IE"中时，断言Flase
        """
        try:
            if browser == "firefox" or browser == "Firefox":
                self.driver = webdriver.Firefox()
            elif browser == "chrome" or browser == "Chrome":
                self.driver = webdriver.Chrome()
            elif browser == "ie" or browser == "IE":
                self.driver = webdriver.Ie()
            self.driver.implicitly_wait(wait_time)
        except Exception:
            self.logger.error("Not found this browser,You can enter 'firefox', 'chrome', 'ie'.")
            assert False

    def initMultitaskDriver(self, browser='firefox', serverUrl='http://127.0.0.1:4444/wd/hub', wait_time=5):
        try:
            if browser == "firefox" or browser == "Firefox":
                self.driver = webdriver.Remote(command_executor=serverUrl,
                                               desired_capabilities=DesiredCapabilities.FIREFOX)
            elif browser == "chrome" or browser == "Chrome":
                self.driver = webdriver.Remote(command_executor=serverUrl,
                                               desired_capabilities=DesiredCapabilities.CHROME)

            elif browser == "ie" or browser == "IE":
                self.driver = webdriver.Remote(command_executor=serverUrl,
                                               desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            self.driver.implicitly_wait(wait_time)
        except Exception:
            self.logger.error("Not found this browser,You can enter 'firefox', 'chrome', 'ie'.")
            assert False

    def get(self, url):
        """
        打开某网址

        举例:打开网址百度
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        将当前页面最大化.

        举例:将当前页面最大化
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        设置浏览器的大小.

        举例:设置浏览器的大小为宽1000,高1000
        driver.set_window_size(1000,1000)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, secsonds):
        """
        设置显示等待时间.

        举例:等待10s
        driver.wait(10)
        """
        self.driver.implicitly_wait(secsonds)

    def find_element(self, element):
        """
        选择定位方式并且定位元素，利用"="号连接

        举例:
        driver.find_element("id=kw")
        """
        if "=" not in element:
            self.logger.error("SyntaxError: invalid syntax, lack of '='.")
            assert False
        else:
            try:
                """
                    根据输入获取元素类型和对应路径
                    类型："id"，"name"，"class"，"text"，"xpath"，"css"
                """
                by = element[0: element.find("=")]
                value = element[element.find("=") + 1: len(element)]

                if by == "id":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.ID, value)))
                    return self.driver.find_element_by_id(value)
                elif by == "name":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.NAME, value)))
                    return self.driver.find_element_by_name(value)
                elif by == "class":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, value)))
                    return self.driver.find_element_by_class_name(value)
                elif by == "text":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.LINK_TEXT, value)))
                    return self.driver.find_element_by_link_text(value)
                elif by == "xpath":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.XPATH, value)))
                    return self.driver.find_element_by_xpath(value)
                elif by == "css":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                    return self.driver.find_element_by_css_selector(value)
                else:
                    self.logger.error(
                        "Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
                    assert False
            except Exception:
                # self.imgs.append(self.driver.get_screenshot_as_base64())
                self.logger.exception("Time out can not find the element,the screen shot is:" + self.get_screenshot())
                assert False

    def find_elements(self, element, index):
        """
        判断元素定位方式和索引，返回元素。

        举例:找到id为kw的元素的第一个，并返回
        driver.find_element("id=kw",1)
        """
        if "=" not in element:
            self.logger.error("SyntaxError: invalid syntax, lack of '='.")
            assert False
        else:
            try:
                by = element[0: element.find("=")]
                value = element[element.find("=") + 1:len(element)]

                if by == "id":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.ID, value)))
                    return self.driver.find_elements_by_id(value)[index]
                elif by == "name":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.NAME, value)))
                    return self.driver.find_elements_by_name(value)[index]
                elif by == "class":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, value)))
                    return self.driver.find_elements_by_class_name(value)[index]
                elif by == "text":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.LINK_TEXT, value)))
                    return self.driver.find_elements_by_link_text(value)[index]
                elif by == "xpath":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.XPATH, value)))
                    return self.driver.find_elements_by_xpath(value)[index]
                elif by == "css":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                    return self.driver.find_elements_by_css_selector(value)[index]
                elif by == "tagName":
                    WebDriverWait(self.driver, self.seconds, 1).until(
                        EC.visibility_of_element_located((By.TAG_NAME, value)))
                    return self.driver.find_elements_by_tag_name(value)[index]
                else:
                    self.logger.error(
                        "Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")
                    assert False
            except Exception:
                self.logger.exception("Time out can not find the element,the screen shot is:" + self.get_screenshot())
                assert False

    def send_keys(self, element, text):
        """
        定位元素并输入文本.
        举例:定位id为kw的文本框，输入selenium
        driver.send_keys("id=kw","selenium")
        """
        element = self.find_element(element)
        element.clear()
        element.send_keys(text)

    def send_keyBoardsEvent(self, element, keyEvent):
        """
        键盘事件操作.

        举例:定位id为kw，按回车
        driver.send_keyBoardsEvent("id=kw","Keys.ENTER")
        """
        self.find_element(element).send_keys(keyEvent)

    def send_keys_index(self, element, index, text):
        """
        先清除然后再输入。

        举例:清除后输入selenium
        driver.send_keys_index("id=kw",5,"selenium")
        """
        element = self.find_elements(element, index)
        element.clear()
        element.send_keys(text)

    def click(self, element):
        """
        定位元素并点击

        举例:定位id为kw的元素并点击
        driver.click("id=kw")
        """
        self.find_element(element).click()

    def click_index(self, element, index):
        """
        找到第几个元素并点击

        举例:点击第5个id为kw的元素
        driver.click_index("id=kw",5)
        """
        self.find_elements(element, index).click()

    def right_click(self, element):
        """
        找到元素点击鼠标右键

        举例:
        driver.right_click("class=right")
        """
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    def move_to_element(self, element):
        """
        将鼠标移动到元素上

        举例:将鼠标移动到css为choose的元素上
        driver.move_to_element("css=choose")
        """
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    def double_click(self, element):
        """
        找到元素双击.

        举例:双击name是baidu的元素
        driver.double_click("name=baidu")
        """
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        将元素拖到目标地址.

        举例:将id为s的元素拖拽到id为t的元素上
        driver.drag_and_drop("id=s","id=t")
        """
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
                                                self.find_element(target_element)).perform()

    def back(self):
        """
        返回上一页，相当于浏览器最上部的左箭头.

        举例:返回上一页
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        前进到下一页，相当于浏览器最上部的右箭头.

        举例:前进到下一页
        driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        得到元素属性的值。

        举例:获取id为kw元素的属性值
        driver.get_attribute("id=kw","attribute")
        """
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        得到元素的文本内容.

        举例:
        driver.get_text("name=johnny")
        """
        return self.find_element(element).text

    def get_display(self, element):
        """
        判断要获取显示的元素是否可现实，返回结果为true或false。

        举例:判断id为app的元素是否可现实
        driver.get_display("id=ppp")
        """
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        获得网页标题.

        举例:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        获取当前页的URL地址。

        举例:
        driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot_as_base64(self):
        return self.driver.get_screenshot_as_base64()

    def get_screenshot(self):
        """
        截图，并保存

        举例:获取当前页面的截图
        driver.get_screenshot()
        """
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        current_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        pic_path = os.path.abspath(os.path.dirname(os.getcwd())) + "\\result\\screenshot\\" + current_date
        pic_name = current_time + '.png'
        if os.path.exists(pic_path):
            pass
        else:
            # 创建多层级的文件夹
            os.makedirs(pic_path)
        self.driver.get_screenshot_as_file(pic_path + '\\' + pic_name)
        return pic_path + '\\' + pic_name

    def submit(self, element):
        """
        表达提交.

        举例:
        driver.submit("id=mainFrame")
        """
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        切换frame.

        举例:切换到id为mainFrame的frame中
        driver.switch_to_frame("id=mainFrame")
        """
        self.driver.switch_to.frame(self.find_element(element))

    def switch_to_frame_out(self):
        """
        这是switch_to中独有的方法，可以切换到上一层的frame，对于层层嵌套的frame很有用。

        举例:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.parent_frame()

    def switch_to_default(self):
        """
        切换到最上层页面。

        举例:
        driver.switch_to_default()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self):
        """
        打开新窗口并切换到新打开的窗口。

        举例:
        driver.open_new_window()
        """
        current_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def F5(self):
        """
        刷新当前页面

        举例:
        driver.F5()
        """
        self.driver.refresh()

    def js(self, script):
        """
        执行JavaScript脚本。

        举例:执行js滚动到指定坐标
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        点击警告框。

        举例:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        解除可用警报。

        举例:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        关闭当前页面
        举例:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        关闭所有页面

        举例:
        driver.quit()
        """
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    # from BlueRose import BlueRose
    # driver = BlueRose("chrome")  # 调用浏览器，支持 'firefox', 'chrome', 'ie' or 'phantomjs'
    driver = BlueRose(browser="chrome")
    driver.get("http://www.baidu.com")
    driver.max_window()  # 浏览器最大化
    driver.send_keys("id=kw", "selenium")  # 该元素位置输入内容
    time.sleep(2)
    driver.click("id=su")
    time.sleep(2)
    driver.click("id=result_logo")  # 点击元素
    time.sleep(2)
    driver.F5()  # 刷新页面
    driver.get_screenshot()  # 截图
    time.sleep(2)
    driver.back()  # 后退
    time.sleep(2)
    driver.forward()  # 前进
    driver.close()
