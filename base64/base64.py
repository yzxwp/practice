import os, pybase64


if __name__ == '__main__':
    # 图片装换
    with open("./1.png", "rb") as f:
        # 将读取的二进制文件转换为base64字符串
        bs64_str = pybase64.b64encode(f.read())
        # 打印图像转换base64格式的字符串,type结果为<class 'bytes'>
        print(bs64_str,'------------', type(bs64_str))
        # 将base64格式的数据装换为二进制数据
        # imgdata = base64.b64decode(bs64_str)
        # # 将二进制数据装换为图片
        # with open("./1.png", "wb") as f2:
        #     f2.write(imgdata)