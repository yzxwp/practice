if __name__ == '__main__':
    for i in range(7500002,8500001):
        print(str(i)+';H '+str(i)+'000;'+str(i)+'@126.com;4600331986'+str(i)+'X;1;发生成功;1602323163886')
        data=str(i)+';H '+str(i)+'000;'+str(i)+'.com;4600331986'+str(i)+'X;1;发生成功;1602323163886'
        # 前面省略，从下面直奔主题，举个代码例子：
        result2txt = str(data)  # data是前面运行出的数据，先将其转为字符串才能写入
        with open('E:/2500wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
            file_handle.write(result2txt)  # 写入
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据