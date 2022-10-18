from Users import *


# 学生类（Users类[用户类]的子类）
class Student(Users):
    student_list = []  # 定义学生列表，管理学生
    sc_list = []  # 定义选课列表
    scl_list = []  # 存放不同学生选课列表的列表
    current_student_index = -1  # 当前登录学生在学生列表中的索引
    current_student_name = ''  # 当前登录学生的姓名

    def __init__(self, studentId, studentName, passWord):
        Users.__init__(self, studentId, studentName, passWord)
        self.student_list.append(self)
        for i in range(len(Student.student_list)):
            self.scl_list.append([])

    def __str__(self):
        return '[学生ID（学号）：' + self.userId + '，姓名:' + self.userName + ']'

    # 学生登录验证
    def student_login(self):
        times = 3  # 三次登录机会
        while True:
            times -= 1
            studentId = input("请输入学号：")
            passWord = input("请输入密码：")
            sId_list = []  # 学生学号列表
            spwd_list = []  # 学生密码列表
            for i in Student.student_list:
                sId_list.append(i.userId)
                spwd_list.append(i.passWord)
            if studentId in sId_list and passWord in spwd_list:
                for i in Student.student_list:
                    if studentId == i.userId:
                        Student.current_student_index = Student.student_list.index(i)
                        Student.current_student_name = Student.student_list[Student.current_student_index].userName
                        Student.sc_list = Student.scl_list[Student.current_student_index]
                print("【提示】学生登录成功~")
                break
            else:
                print(f"【提示】学号/密码错误，请重新输入！（你还剩{times}次登录机会）")
            if times <= 0:
                print("【警告】输入错误次数已超过三次，强制退出系统~")
                exit()  # 退出整个系统（程序）

    # 1、课程信息浏览
    def show_all_courses(self):
        print(
            "-----------------------------------------------------------------------------------------------------------"
            "\n课程编号\t\t课程名称\t\t\t课程性质\t\t总学时\t\t授课学时\t\t实验或上机学时\t学分\t\t开课学期"
            "\n-----------------------------------------------------------------------------------------------------------")
        # 通过course.txt文件读取总课程列表
        f = open('course.txt', 'r', encoding='utf-8', errors='ignore')  # 统一使用utf-8编码，解决读写时编码不统一（GBK）的问题
        course_list = f.read()
        course_list = eval(course_list)  # 将读出的字符串转化成列表类型
        for i in course_list:
            print(
                f"{i['cId']}\t\t\t{i['cName']:<10}\t{i['cProperty']}\t\t{i['cTotalTime']}\t\t\t{i['cTeachTime']}\t\t\t"
                f"{i['cTrailTime']}\t\t\t\t{i['cCredit']}\t\t{i['cDate']}")
        f.close()

    # 2、查询某一课程信息(课程编号查找)
    def search_someone_course(self):
        cId = int(input("【亲爱的同学】请输入要查找的课程编号："))
        print(
            "                                            ***** 所查课程 *****                                              "
            "\n-----------------------------------------------------------------------------------------------------------"
            "\n课程编号\t\t课程名称\t\t\t课程性质\t\t总学时\t\t授课学时\t\t实验或上机学时\t学分\t\t开课学期"
            "\n-----------------------------------------------------------------------------------------------------------")
        course_list = Users.load_course(self)  # 加载（读取）过去已经录入的课程信息
        cId_list = []  # 定义课程编号（ID）列表
        for i in course_list:
            cId_list.append(i['cId'])
        if_have = Users.LinearSearch(cId_list, cId)  # 所查课程是否存在(线性查找算法)
        if not if_have:
            print(f"{'【提示】查无此课程！':^100}")
        else:
            for i in course_list:
                if cId == i['cId']:
                    print(
                        f"{i['cId']}\t\t\t{i['cName']:<10}\t{i['cProperty']}\t\t{i['cTotalTime']}\t\t\t{i['cTeachTime']}\t\t\t"
                        f"{i['cTrailTime']}\t\t\t\t{i['cCredit']}\t\t{i['cDate']}")
                    break

    # 3、选课
    def select_course(self):
        Student.show_all_courses(self)
        cId = int(input("【亲爱的同学】请输入你要选修的课程编号(输入0退出)："))
        if cId == 0:
            return  # 退出选课函数
        print(
            "-----------------------------------------------------------------------------------------------------------"
            "\n课程编号\t\t课程名称\t\t\t课程性质\t\t总学时\t\t授课学时\t\t实验或上机学时\t学分\t\t开课学期"
            "\n-----------------------------------------------------------------------------------------------------------")
        course_list = Users.load_course(self)  # 加载（读取）过去已经录入的课程信息
        cId_list = []  # 定义课程编号（ID）列表
        for i in course_list:
            cId_list.append(i['cId'])
        if_have = Users.LinearSearch(cId_list, cId)  # 所查课程是否存在(线性查找算法)
        if not if_have:
            print(f"{'【提示】选课失败！无此课程，请重选！':^100}\n")
            Student.select_course(self)
        for i in course_list:
            if cId == i['cId']:
                print(
                    f"{i['cId']}\t\t\t{i['cName']:<10}\t{i['cProperty']}\t\t{i['cTotalTime']}\t\t\t{i['cTeachTime']}\t\t\t"
                    f"{i['cTrailTime']}\t\t\t\t{i['cCredit']}\t\t{i['cDate']}")
                if_select = input("【提示】是否确认选择该课程？(y/n)")  # 是否确认选课
                if if_select == 'y' and i not in Student.sc_list:
                    Student.sc_list.append(i)
                    print(f"【提示】已成功选择[{i['cId']}:{i['cName']}]课程！")
                    Student.select_course(self)
                elif if_select == 'y' and i in Student.sc_list:
                    print("【提示】选课失败！该课程已选，不能重复选择！")
                    Student.select_course(self)
                elif if_select == 'n':
                    print("【提示】已取消选择该课程...")
                    Student.select_course(self)
                else:
                    print("【警告】输入不合法，已取消选择该课程...")
                    Student.select_course(self)
                break

    # 4、查看已选课程
    def search_selected_course(self):
        print(
            "                                            ***** 已选课程 *****                                              "
            "\n-----------------------------------------------------------------------------------------------------------"
            "\n课程编号\t\t课程名称\t\t\t课程性质\t\t总学时\t\t授课学时\t\t实验或上机学时\t学分\t\t开课学期"
            "\n-----------------------------------------------------------------------------------------------------------")
        total_cCredit = 0  # 已选课程总学分
        for i in Student.sc_list:
            print(
                f"{i['cId']}\t\t\t{i['cName']:<10}\t{i['cProperty']}\t\t{i['cTotalTime']}\t\t\t{i['cTeachTime']}\t\t\t"
                f"{i['cTrailTime']}\t\t\t\t{i['cCredit']}\t\t{i['cDate']}")
            total_cCredit += i['cCredit']
        print(f"【提示|总学分需>=60】当前已选课程总学分：{total_cCredit}")
        if total_cCredit < 60:
            print("【严重警告】当前已选课程总学分少于60，请继续选课！\n")
            Student.select_course(self)
        else:
            print("【温馨提示】当前已选课程总学分已达60，可继续选课，或输入5退出选课~")


student01 = Student('111', '小熊', '111')
student02 = Student('222', '小杨', '222')
student03 = Student('333', '小煜', '333')
student04 = Student('444', '小郭', '444')
student05 = Student('555', '小域', '555')
