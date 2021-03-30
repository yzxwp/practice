import random
import string

from framework.UtilsDate import UtilsDate


class UtilsRandom(object):
    # 随机生成中文姓名
    # 装饰器  静态方法，类名直接调用静态方法，不需要实例化对象，通常用在公共的工具类设计中
    @staticmethod
    def getChineseName():
        first_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                       '许',
                       '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                       '庞',
                       '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        last_names = random.randint(0x4e00, 0x9fbf)
        return random.choice(first_names) + chr(last_names) +str(UtilsDate.getTimeStamp())

    # 随机生成手机号码
    @staticmethod
    def getMobilePhone():
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        # return random.choice(prelist) + str(''.join(random.sample(string.digits, 8)))

    @staticmethod
    def getGradeId():
        grade_id = ['大一', '大二','大三']
        return random.choice(grade_id)

    @staticmethod
    def getSex():
        sex = ['男', '女']
        return random.choice(sex)


    @staticmethod
    def getClassId():
        classid = ['1班', '2班','3班']
        return random.choice(classid)

    # 随机生成身份证号
    @staticmethod
    def getIdCard():
        idcard ="".join(random.choice("0123456789") for i in range(18))
        return idcard

    # 随机生成成绩
    @staticmethod
    def getGrade():
        grade = random.randint(30,100)
        return grade


    # 随机生成邮箱
    @staticmethod
    def getEmail():
        emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
        randomEmail = random.choice(emailtype)
        rang = random.randint(4, 10)
        number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        randomNumber = "".join(random.choice(number) for i in range(rang))
        email = randomNumber + randomEmail
        return email



 # # 随机生成中文名
 #    def getChineseName(self):
 #        first_name_list = [
 #            '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
 #            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
 #            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
 #            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
 #            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
 #            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
 #            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '郭']
 #        n = random.randint(0, len(first_name_list) - 1)
 #        f_name = first_name_list[n]
 #
 #        head = random.randint(0xb0, 0xf7)
 #        body = random.randint(0xa1, 0xfe)
 #        val = f'{head:x} {body:x}'
 #        l_name = bytes.fromhex(val).decode('gb2312')
 #        name = f_name + l_name
 #        return name
 #
 #    # 随机生成手机号
 #    def getMobilePhone(self):
 #        list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
 #                   "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
 #                   "186", "187", "188", "189"]
 #        phone = random.choice(list) + str(random.randint(00000000, 99999999))
 #        return phone
 #
 #    # 随机生成邮箱
 #    def getEmail(self):
 #        emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
 #        email = ''.join(random.sample(string.hexdigits,8)) + random.choice(emailtype)
 #        return email

if __name__ == '__main__':
    print(UtilsRandom.getIdCard())
    print("随机获取的中文名：" + UtilsRandom.getChineseName())
    # print(''.join(['dsf','sdf','sdf']))
    UtilsRandom.getMobilePhone()
    # print("随机生成的手机号码：" + UtilsRandom.getMobilePhone())
    # print("随机生成的邮箱：" + UtilsRandom.getEmail())
