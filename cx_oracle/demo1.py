#python 链接oracle数据库采用
'''
简单的使用流程如下：
①.引用模块cx_Oracle
②.连接数据库
③.获取cursor
④.使用cursor进行各种操作
⑤.关闭cursor
⑥.关闭连接
'''
import cx_Oracle as cx
def ssh_oracle():
    sql = str("select location_type from tlb_rent_request t where t.rent_request_code='S2009180003'")
    conn=cx.Connection('NFRZZL/NFRZZL_YWCS@172.26.164.216/DFNFRZZL_YWCS')
    cur=conn.cursor()
    print('我是oracle数据库')

if __name__ == '__main__':
    ssh_oracle()



