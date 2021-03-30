import csv

class UtilsFile:

    # 创建一个空文件
    def creatCsvFile(self,filename):
        f = open('E:\csv文件\{}'.format(filename), 'wb')
        f.close()
        print("创建{}成功".format(filename))


    # 写入csv文件
    def writeCsvFile(self,filepath ,data):
        # "newline="就是说因为我们的csv文件的类型，如果不加这个东西，当我们写入东西的时候，就会出现空行
        csvfile = open(filepath, 'a+', newline='')
        # 获得对象
        writer = csv.writer(csvfile)
        # 写入多行  写入单行用writer.writerow
        writer.writerows(data)
        # 关闭
        csvfile.close()
        print("write over")

    # 读取csv文件
    def readCsvFile(self, filepath):
        csvfile = open(filepath, 'r', newline='')
        # 获得对象
        csvReader = csv.reader(csvfile)
        #print(csvReader)
        # 读取内容并打印
        for content in csvReader:
            print(content)
        # 关闭
        csvfile.close()

if __name__ == '__main__':
    file = UtilsFile()
    #file.creatCsvFile("test.csv")
    filepath = r"E:\csv文件\test.csv"
    #data = [('姓名', '年龄'), ('张三', '22'), ('李四', '22')]
    #data = [('王五', '25')]
    #file.writeCsvFile(filepath, data)
    file.readCsvFile(filepath)
