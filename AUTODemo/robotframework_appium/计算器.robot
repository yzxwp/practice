*** Settings ***
Suite Setup       appnium与手机建立连接并打开计算器
Suite Teardown    关闭程序
Library           AppiumLibrary

*** Test Cases ***
模拟计算器加法
    选择键盘1并点击
    选择键盘2并点击
    选择键盘4并点击
    选择键盘+并点击
    选择键盘9并点击
    选择键盘7并点击
    选择键盘=并点击

模拟计算器减法
    选择键盘1并点击
    选择键盘2并点击
    选择键盘4并点击
    选择键盘-并点击
    选择键盘9并点击
    选择键盘7并点击
    选择键盘=并点击

模拟计算器除法
    选择键盘1并点击
    选择键盘2并点击
    选择键盘4并点击
    选择键盘%并点击
    选择键盘4并点击
    选择键盘=并点击

模拟计算器乘法
    选择键盘1并点击
    选择键盘2并点击
    选择键盘4并点击
    选择键盘*并点击
    选择键盘7并点击
    选择键盘=并点击

*** Keywords ***
appnium与手机建立连接并打开计算器
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=7.0    deviceName=JGB9K17B07905329    appPackage=com.android.calculator2    appActivity=Calculator    #unicodeKeyboard=True    resetKeyboard=True
    log    与手机建立连接成功

关闭程序
    log    关闭程序
    Close Application

选择键盘1并点击
    log    点击1
    Click Element    id=com.android.calculator2:id/digit_1

选择键盘2并点击
    log    点击2
    Click Element    id=com.android.calculator2:id/digit_2

选择键盘3并点击
    log    点击3
    Click Element    id=com.android.calculator2:id/digit_3

选择键盘4并点击
    log    点击4
    Click Element    id=com.android.calculator2:id/digit_4

选择键盘5并点击
    log    点击5
    Click Element    id=com.android.calculator2:id/digit_5

选择键盘6并点击
    log    点击6
    Click Element    id=com.android.calculator2:id/digit_6

选择键盘7并点击
    log    点击7
    Click Element    id=com.android.calculator2:id/digit_7

选择键盘8并点击
    log    点击8
    Click Element    id=com.android.calculator2:id/digit_8

选择键盘9并点击
    log    点击9
    Click Element    id=com.android.calculator2:id/digit_9

选择键盘0并点击
    log    点击0
    Click Element    id=com.android.calculator2:id/digit_10

选择键盘+并点击
    log    点击+号
    Click Element    id=com.android.calculator2:id/op_add

选择键盘-并点击
    log    点击-号
    Click Element    id=com.android.calculator2:id/op_sub

选择键盘*并点击
    log    点击*号
    Click Element    id=com.android.calculator2:id/op_mul

选择键盘%并点击
    log    点击%号
    Click Element    id=com.android.calculator2:id/op_div

选择键盘=并点击
    log    点击=号
    Click Element    id=com.android.calculator2:id/eq

清除输入内容
    log    点击清除键
    Click Element    id=com.android.calculator2:id/op_clr
