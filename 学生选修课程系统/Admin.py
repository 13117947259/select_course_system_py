from Student import *
from Course import *


# 管理员类（Users类[用户类]的子类）
class Admin(Users):
    def __init__(self, adminId, adminName, passWord):
        Users.__init__(self, adminId, adminName, passWord)

    # 管理员登录验证
    def admin_login(self):
        times = 3  # 三次登录机会
        while True:
            times -= 1
            adminId = input("请输入管理员账号：")
            passWord = input("请输入密码：")
            if adminId == admin01.userId and passWord == admin01.passWord:
                print("【提示】管理员登录成功~")
                break
            else:
                print(f"【提示】管理员账号/密码错误，请重新输入！（你还剩{times}次登录机会）")
            if times <= 0:
                print("【警告】输入错误次数已超过三次，强制退出系统~")
                exit()

    # 1、课程信息录入
    def add_course(self):
        course_list = Users.load_course(self)  # 加载（读取）过去已经录入的课程信息
        cId_list = []  # 课程编号（ID）列表，用于验证新录入课程是否存在
        for i in course_list:
            cId_list.append(i['cId'])
        cId = int(input("请输入课程编号："))
        # 判断新录入课程是否存在，如果存在则不进行后续录入操作
        if cId in cId_list:
            print("【警告】该课程（编号）已存在，请勿重复录入哦！")
            return Admin.add_course(self)
        # 后续录入操作
        cName = input("请输入课程名称：")
        cProperty = input("请输入课程性质：")
        cTotalTime = int(input("请输入总学时："))
        cTeachTime = int(input("请输入授课学时："))
        cTrailTime = int(input("请输入实验或上机学时："))
        cCredit = int(input("请输入学分："))
        cDate = input("请输入开课学期：")
        new_course = Course(cId, cName, cProperty, cTotalTime, cTeachTime, cTrailTime, cCredit, cDate)  # 创建新录入课程对象实例
        course_list.append(new_course.__dict__)  # 将新录入课程（字典形式）添加到总课程列表
        # 将总课程列表（原课程列表+新录入课程）写入到course.txt文件中
        f = open('course.txt', 'w', encoding='utf-8', errors='ignore')
        f.write(str(course_list))
        f.close()
        print(f"【提示】课程[{new_course.cId}:{new_course.cName}]录入成功！")

    # 2、课程信息浏览
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

    # 3、查询某一学生选课信息（学生id查找）
    def search_someone_sc(self):
        sId = input("【尊敬的管理员】请输入要查找的学生ID（学号）：")
        sId_list = []  # 定义学生学号（ID）列表
        for i in Student.student_list:
            sId_list.append(i.userId)
        if_have = Users.LinearSearch(sId_list, sId)  # 所查学生是否存在(线性查找算法)
        if not if_have:
            print(f"{'【提示】查无此人（学生）！':^100}")
        else:
            for j in Student.student_list:  # j：学生对象实例
                if sId == j.userId:
                    print(
                        f"                           ***** {j.__str__()} 已选课程 *****                                             "
                        "\n-----------------------------------------------------------------------------------------------------------"
                        "\n课程编号\t\t课程名称\t\t\t课程性质\t\t总学时\t\t授课学时\t\t实验或上机学时\t学分\t\t开课学期"
                        "\n-----------------------------------------------------------------------------------------------------------")
                    for i in Student.scl_list[Student.student_list.index(j)]:  # i：选课列表中的单个课程（字典类型）
                        print(
                            f"{i['cId']}\t\t\t{i['cName']:<10}\t{i['cProperty']}\t\t{i['cTotalTime']}\t\t\t{i['cTeachTime']}\t\t\t"
                            f"{i['cTrailTime']}\t\t\t\t{i['cCredit']}\t\t{i['cDate']}")
                    if Student.scl_list[Student.student_list.index(j)] == []:
                        print("【警告】该学生暂无选课！请尽快催促~")
                    break

    # 4、查看所有学生选课信息
    def search_all_sc(self):
        for j in Student.student_list:  # j：学生对象实例
            print(
                f"\n                           ***** {j.__str__()} 已选课程 *****                                             "
                "\n-----------------------------------------------------------------------------------------------------------"
                "\n课程编号\t\t课程名称\t\t\t课程性质\t\t总学时\t\t授课学时\t\t实验或上机学时\t学分\t\t开课学期"
                "\n-----------------------------------------------------------------------------------------------------------")
            for i in Student.scl_list[Student.student_list.index(j)]:  # i：选课列表中的单个课程（字典类型）
                print(
                    f"{i['cId']}\t\t\t{i['cName']:<10}\t{i['cProperty']}\t\t{i['cTotalTime']}\t\t\t{i['cTeachTime']}\t\t\t"
                    f"{i['cTrailTime']}\t\t\t\t{i['cCredit']}\t\t{i['cDate']}")
            if Student.scl_list[Student.student_list.index(j)] == []:  # 学生选课列表为空
                print("【警告】该学生暂无选课！请尽快催促~")


admin01 = Admin("admin", "占老师", "admin")
