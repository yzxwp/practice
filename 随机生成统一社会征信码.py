# encoding=utf8
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#生成虚拟的企业：组织机构代码（八位数字（或大写拉丁字母）本体代码和一位数字（或大写拉丁字母）校验码组成）
    三证合一和一证一码是指工商营业执照，税务登记证，组织机构代码证合并为一张加载统一社会信用代码的营业执照。
    统一社会信用代码：（登记管理部门代码（1位）、机构类别代码（1位）、登记管理机关行政区划码（6位）、主体标识码（组织机构代码）（9位）和校验码（1位）5个部分组成）
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

# 统一社会信用代码最后一位：代码字符集
check_dict = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "J": 18, "K": 19, "L": 20, "M": 21,
    "N": 22, "P": 23, "Q": 24, "R": 25, "T": 26, "U": 27, "W": 28, "X": 29, "Y": 30
}
dict_check = {value: key for key, value in check_dict.items()}


# 组织机构代码 9位
def create_organization():
    weight_code = [3, 7, 9, 10, 5, 8, 4, 2]  # Wi 代表第i位上的加权因子=pow(3,i-1)%31
    org_code = []  # 组织机构代码列表
    sum = 0
    for i in range(8):
        org_code.append(dict_check[random.randint(0, 30)])  # 前八位本体代码：0~9 + A~Z 31个
        sum = sum + check_dict[org_code[i]] * weight_code[i]
    C9 = 11 - sum % 11  # 代表校验码：11-MOD（∑Ci(i=1→8)×Wi,11）-->前8位加权后与11取余，然后用11减
    if C9 == 10:
        last_code = 'X'
    elif C9 == 11:
        last_code = '0'
    else:
        last_code = str(C9)

    code = ''.join(org_code) + '-' + last_code  # 组织机构代码
    # print(code)
    return code


# 统一社会信用代码 18位
sum = 0
def create_social_credit():
    manage_code = [9]  # 登记管理部门代码：9-工商
    type_code = [1, 2, 3, 9]  # 9-1-企业，9-2-个体工商户，9-3-农民专业合作社，9-9-其他
    area_code = '100000'  # 登记管理机关行政区划码：100000-国家用
    org_code = create_organization().replace('-', '')  # 组织机构代码
    sum = 0
    weight_code = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]  # Wi 代表第i位上的加权因子=pow(3,i-1)%31
    code = str(random.choice(manage_code)) + str(random.choice(type_code)) + area_code + org_code
    for i in range(17):
        sum = sum + check_dict[code[i:i + 1]] * weight_code[i]
    try:
        C18 = dict_check[31 - sum % 31]
    except:
        return create_social_credit()
    social_code = code + C18
    return social_code

if __name__ == '__main__':
    count=0
    for i in range(0,1000000):
        count+=1
        print(create_organization())