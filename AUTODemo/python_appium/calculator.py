# encoding:utf-8
import unittest
from appium import webdriver
from python_appium.calculatorPage import CalculatorPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7'
        desired_caps['deviceName'] = 'JGB9K17B07905329'
        desired_caps['appPackage'] = "com.android.calculator2"
        desired_caps['appActivity'] = ".Calculator"
        desired_caps['automationName'] = "uiautomator2"
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.calcuator = CalculatorPage(cls.driver)

    def tearDown(self):
        self.calcuator.button_clear.click()

    def test_1234_add_5678(self):
        self.calcuator.button1.click()
        self.calcuator.button2.click()
        self.calcuator.button3.click()
        self.calcuator.button4.click()
        self.calcuator.button_jia.click()
        self.calcuator.button5.click()
        self.calcuator.button6.click()
        self.calcuator.button7.click()
        self.calcuator.button8.click()
        self.calcuator.button_dengyu.click()
        act = self.calcuator.button_text
        excp = "6,912"
        self.assertEqual(excp, act)

    def test_5678_jian_1234(self):
        self.calcuator.button5.click()
        self.calcuator.button6.click()
        self.calcuator.button7.click()
        self.calcuator.button8.click()
        self.calcuator.button_jian.click()
        self.calcuator.button1.click()
        self.calcuator.button2.click()
        self.calcuator.button3.click()
        self.calcuator.button4.click()
        self.calcuator.button_dengyu.click()
        act = self.calcuator.button_text
        excp = "4,444"
        self.assertEqual(excp, act)

    def test_1234_cheng_5678(self):
        self.calcuator.button1.click()
        self.calcuator.button2.click()
        self.calcuator.button3.click()
        self.calcuator.button4.click()
        self.calcuator.button_cheng.click()
        self.calcuator.button5.click()
        self.calcuator.button6.click()
        self.calcuator.button7.click()
        self.calcuator.button8.click()
        self.calcuator.button_dengyu.click()
        act = self.calcuator.button_text
        excp = "7,006,652"
        self.assertEqual(excp, act)

    @unittest.skip("test_9999_chu_3333")
    def test_9999_chu_3333(self):
        self.calcuator.button9.click()
        self.calcuator.button9.click()
        self.calcuator.button9.click()
        self.calcuator.button9.click()
        self.calcuator.button_chu.click()
        self.calcuator.button3.click()
        self.calcuator.button3.click()
        self.calcuator.button3.click()
        self.calcuator.button3.click()
        self.calcuator.button_dengyu.click()
        act = self.calcuator.button_text
        excp = "3"
        self.assertEqual(excp, act)


if __name__ == '__main__':
    # 创建一个容器suite
    suite = unittest.TestSuite()
    # 往容器中增添case 类的名字：test_1234_add_5678
    suite.addTest(MyTestCase('test_1234_add_5678'))
    suite.addTest(MyTestCase('test_5678_jian_1234'))
    suite.addTest(MyTestCase('test_1234_cheng_5678'))
    suite.addTest(MyTestCase('test_9999_chu_3333'))
    # 执行
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # unittest.main()


