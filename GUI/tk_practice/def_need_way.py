# encoding:utf-8
import 随机获得身份证号码 as id_card
import 随机生成统一社会征信码 as id_credit
import 随机生成电话号码 as phone
import 随机获得姓名 as name
import 随机获得车架号VIN as vin
import 随机获得银行卡号 as bank_card


# 获得用户姓名
def text_name(END):
    text_name.delete('0.0', END)
    text_name.insert('0.0', name.random_name())


# 获得手机号码
def text_phone():
    return phone.phone_num()


# 获得身份证号码
def text_idcard():
    return id_card.main()


# 获得统一社会征信码
def text_tyshzxm():
    return id_credit.create_social_credit()


# 获得组织机构代码
def text_zzjgdm():
    return id_credit.create_organization()


# 获得随机获得车架号
def text_vin():
    return vin.random_vin()

# 获得随机获得工行银行卡
def text_bank_gon():
    return bank_card.gen_bank_card_nonghang()
# 获得随机获得农行银行卡
def text_bank_non():
    return bank_card.gen_bank_card_gonghang()
