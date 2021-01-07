# author:闫振兴
# contact: 1753502691@qq.com
# datetime:2020/6/29 21:18
# software: PyCharm
"""
文件说明：
"""
#encoding:utf-8
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

print("链接手机")
device=mr.waitForConnection()

print("安装app")
device.installPackage(r"C:\Users\dell\PycharmProjects\AUTODemo\monkey\app-release(3).apk")

print("打开手机")
package="com.nfrzzlapp"
activity="com.nfrzzlapp.MainActivity"
runComponent=package+'/'+activity
device.startActivity(component=runComponent)

mr.sleep(10)
device.touch(558,1110,"DOWN_AND_UP")
mr.sleep(2)
device.touch(552,1110,"DOWN_AND_UP")
mr.sleep(2)
device.touch(479,1142,"DOWN_AND_UP")
mr.sleep(2)
device.touch(275,560,"DOWN_AND_UP")
mr.sleep(2)
device.type("123101")
mr.sleep(2)
device.touch(345,659,"DOWN_AND_UP")
mr.sleep(2)
device.type("123321")
mr.sleep(2)
device.touch(392,562,"DOWN_AND_UP")
mr.sleep(2)
screenshot=device.takeSnapshot()
screenshot.writeToFile(r"C:\Users\dell\PycharmProjects\AUTODemo\monkey\nfrzzlapp.png","png")






