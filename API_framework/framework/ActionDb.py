import pymysql


class ActionDb():


    def queryTable(self,sql):
        # 连接数据库
        conn = pymysql.connect('localhost', user='root', passwd='root', db='test')
        # 获取游标
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


        print('sql执行成功')
        return cursor.fetchall()




    # 删除数据
    def delTable(self,sql):
        # 连接数据库
        conn = pymysql.connect('localhost', user='root', passwd='root', db='test')
        # 获取游标
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print('sql执行成功')

if __name__ == '__main__':
    print(ActionDb().queryTable('select student_id from student where student_name="刘龙";'))