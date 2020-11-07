from PIL import Image
import math
import operator
from functools import reduce
from PIL import ImageChops


def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        diff.save(diff_save_location)
    except ValueError as e:
        text = ("图片大小和box对应的宽度不一致")
        return text


def image_contrast(img1, img2, diff_save_location):
    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    if result == 0.0:
        return "We are the same!"
    else:
        return compare_images(img1, img2, diff_save_location)


if __name__ == '__main__':
    # img1 = "1.png"  # 指定图片路径
    print("请输入两张图片的路径，友情提示：图片类型只能为png，gif且图片宽度相等，\n图片若与exe文件在同一路径下可以直接输入图片名字，如1.png")
    while 1:
        try:
            img1 = input("请输入第一张图片的路径：例如:D:/1.gif：")
            # img2 = "2.png"
            img2 = input("请输入第二张图片的路径：：")
            diff_save_location = "我们不一样.gif"
            try:
                result = image_contrast(img1, img2, diff_save_location)
            except:
                print("两个图片路径错误")
            if result == None:
                print("请查看【我们不一样.gif】")
            else:
                print(result)
        except:
            print("发生错误，再来一次，请按照提示正确操作,注意两张图片的宽度相等")