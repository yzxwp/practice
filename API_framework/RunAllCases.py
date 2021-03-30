#coding: utf-8
import os
import unittest

from unittestreport import TestRunner


class RunAllCases():
    @staticmethod
    def load_running_case():
        # 测试用例的路径
        case_path = os.path.split(os.path.realpath(__file__))[0] + '/testCase/stumanager/'
        # 加载某个路径下面的测试用例
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern='Test*.py',
                                                       top_level_dir=None)

        # print(os.path.realpath(__file__)) # 当前文件的绝对路径
        # print(os.path.split(os.path.realpath(__file__))) # 文件名和路径分割成数组
        # print(os.path.split(os.path.realpath(__file__))[0])
        return discover
if __name__ == "__main__":
    # 测试报告的路径
    report_path = os.path.split(os.path.realpath(__file__))[0] + "\\report"
    if os.path.exists(report_path):
        pass
    else:
        os.makedirs(report_path)
    runner = TestRunner(RunAllCases.load_running_case(),
                        title='学生管理系统测试报告',
                        tester='gqf',
                        filename="Student_AutoTest_Report.html",
                        report_dir= report_path,
                        desc="学生管理系统自动化测试", )

    runner.run()
    runner.send_email(host="smtp.163.com",
                      port=465,
                      user="g2473530026@163.com",
                      password="LPZWLCTLZJOHSGKE",
                      to_addrs="2473530026@qq.com")

