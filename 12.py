if __name__ == '__main__':
    import random
    import string

    print(random.random())  # 随机浮点数，默认取0-1，不能指定范围
    print(random.randint(1, 20))  # 随机整数
    print(random.randrange(1, 20))  # 随机产生一个range
    print(random.choice('x23serw4'))  # 随机取一个元素
    print(random.sample('hello', 2))  # 从序列中随机取几个元素
    print(random.uniform(1, 9))  # 随机取浮点数，可以指定范围
    x = [1, 2, 3, 4, 6, 7]
    random.shuffle(x)  # 洗牌,打乱顺序，会改变原list的值
    print(x)
    print(string.digits)  # 所有的数字
    print(string.ascii_letters)  # 所有的字母
    print(string.punctuation)  # 所有的特殊字符