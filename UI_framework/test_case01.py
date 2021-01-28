import unittest

from selenium import webdriver



class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
