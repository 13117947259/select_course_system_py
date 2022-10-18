# 用户类（是学生类和管理员类的基类）
class Users(object):

    def __init__(self, userId, userName, passWord):
        # 用户ID，用户名，密码
        self.userId = userId
        self.userName = userName
        self.passWord = passWord

    # 加载（读取）过去已经录入的课程信息，方便以列表形式于文件中读写所有课程数据；同时有返回值，返回一个课程列表
    def load_course(self):
        f = open('course.txt', 'r', encoding='utf-8', errors='ignore')
        course_list = f.read()
        f.close()
        return eval(course_list)  # 列表类型

    # 线性查找算法
    def LinearSearch(list, item):
        index = 0
        found = False
        while index < len(list) and found is False:
            if list[index] == item:
                found = True
            else:
                index = index + 1
        return found
