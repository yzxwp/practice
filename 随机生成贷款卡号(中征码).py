import random

power = [1,3,5,7,11,2,13,1,1,17,19,97,23,29]  #权重
arr = []
sum = 0

#随机生成前14位并保存在列表arr中
for i in range(14):
    value = random.randint(0,9)
    arr.append(value)

#前十四位乘以权重相加
for j in range(14):
    value = arr[j] * power[j]
    sum = sum + value

#除以97后的余数再加1
last_two = sum % 97 + 1

#如果此数字为个位数，前面还需要补一个零
if last_two>10:
    shiwei = last_two // 10
    gewei = last_two % 10
    arr.append(shiwei)
    arr.append(gewei)
else:
    shiwei = 0
    gewei = last_two
    arr.append(shiwei)
    arr.append(gewei)

#输出贷款卡号
print("loanCardNo: ",end="")
for i in range(0,16):
    print(arr[i],end="")