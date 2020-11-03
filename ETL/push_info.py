import 随机生成uuid as uid
import 随机获得身份证号码 as idcard
import 随机获得姓名  as name
import 随机生成电话号码 as phone

if __name__ == '__main__':
    t = 1602820800000
    tt = 86400000
    for i in range(1, 18):
        count = 10000
        for j in range(0, (i * 50001 - (i - 1) * 50001)):
            if count < 40000:
                count = count + 1
                data= uid.getUUID()+";;01;1;"+name.random_name() + "|1|" + idcard.main() + "|" + phone.phone_num() + "|H1003029419|2020年06月16日|2686.68|null|null|null|null|null;;1;;;;"+str(t + tt * i)
                print(str(data))
                with open('E:/3wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                    file_handle.write(data)  # 写入
                    file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
            else:
                count = count + 1
                data = uid.getUUID() + ";" + "f2eb6b4a34b3fb" + str(count) + "dbddd;01;1;" + name.random_name() + "|1|" + idcard.main() + "|" + phone.phone_num() + "|H1003029419|2020年06月16日|2686.68|null|null|null|null|null;;1;;;;"+ str(t + tt * i)
                with open('E:/2wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                    file_handle.write(data)  # 写入
                    file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
                print(str(data))