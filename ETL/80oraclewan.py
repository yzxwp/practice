import 随机生成uuid as u
import 随机获得姓名 as name
import 生产随机时间 as t

if __name__ == '__main__':
    for i in range(0,720000):
        data=u.getUUID()+";"+u.getUUID()+';'+u.getUUID()+";"+name.random_name()+''+name.random_name()+";"+name.random_name()+""+name.random_name()+";"+t.get_time()+";"\
    +t.get_time()+";0;1;"+"XTADMIN;"+t.get_time()+";XTADMIN;"+t.get_time()+";"+t.get_time()+";"+t.get_time()+";"+t.get_time()+";"+t.get_time()+";;;;"
        print(data)
        with open('E:/80oraclewan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(data)  # 写入
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
