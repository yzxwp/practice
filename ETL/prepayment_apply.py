import 随机获得身份证号码 as idcard
import 生产随机时间 as t
if __name__ == '__main__':
    for i in range(1000000,2001000):
        data=str(i)+';'+idcard.main()+';P32'+ str(i) +';'+t.get_time()+';'+str(i+69354.97)+';'+str(i+65880)+';180.97;3294;0;0;0;;1603944000000'
        print(data)
        result2txt = str(data)  # data是前面运行出的数据，先将其转为字符串才能写入
        with open('E:/100wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(result2txt)  # 写入
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据