if __name__ == '__main__':
    for i in range(9000001,12000001):
        print(str(i)+'f2eb6b4a34b3fb6343981dbddd;;01;1;谭学杨|1|422822199807172018|15587679009|H1003029419|2020年06月16日|2686.68|null|null|null|null|null;;1;;;;1602227473246')
        data=str(i)+'f2eb6b4a34b3fb6343981dbddd;;01;1;谭学杨|1|422822199807172018|15587679009|H1003029419|2020年06月16日|2686.68|null|null|null|null|null;;1;;;;1602227473246'
        # 前面省略，从下面直奔主题，举个代码例子：
        result2txt = str(data)  # data是前面运行出的数据，先将其转为字符串才能写入
        if i>=0 and i<=1000001:
            with open('E:/100wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i>1000001 and i<=2000001:
            with open('E:/200wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i > 2000001 and i <= 3000001:
            with open('E:/300wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i > 3000001 and i <= 4000001:
            with open('E:/400wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i > 4000001 and i <= 5000001:
            with open('E:/500wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i > 5000001 and i <= 6000001:
            with open('E:/600wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i > 6000001 and i <= 7000001:
            with open('E:/700wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        elif i > 7000001 and i <= 8000001:
            with open('E:/800wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        else:
            with open('E:/900wan.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
                file_handle.write(result2txt)  # 写入
                file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据