import 随机生成uuid as uid
import 随机获得身份证号码 as idcard
import 随机获得姓名  as name
import 随机生成电话号码 as phone

if __name__ == '__main__':
    message='车贷：您合同号H1003029419的车贷月供2686.68元，建议于2020年06月16日十点前存足。微信t.cn/A6w1xn1Q'
    for i in range(1, 10):
        data = uid.getUUID()+";"+ "f2eb6b4a34b3fb6343981dbddd;;01;1;" + \
               name.random_name() + "|1|" + idcard.main() + "|" + phone.phone_num() + "|H1003029419|2020年06月16日|2686.68|null|null|null|null|null;"+message+\
               ";1;1;ADMIN;1604297400453;1602227473246'"
        print(data)