from Menu import *
from Admin import *
from Users import *


# 选课系统类
class ChooseCourseSystem(object):
    def run(self):  # 选课系统运行函数
        while True:
            Users.load_course(self)  # 加载（读取）过去已经录入的课程信息
            Menu.main_menu(self)  # 显示主菜单
            user = input("【】请选择登录角色：")
            # 1.学生登录
            if user == '1':
                Student.student_login(self)  # 学生登录验证
                while True:
                    Menu.student_select_menu(self)  # 显示学生选课菜单（二级菜单）
                    student_operation = input("【亲爱的同学】请输入你的操作：")
                    if student_operation == '1':
                        # 1、课程信息浏览
                        Student.show_all_courses(self)
                    elif student_operation == '2':
                        # 2、查询某一课程信息(课程编号查找)
                        Student.search_someone_course(self)
                    elif student_operation == '3':
                        # 3、选课
                        Student.select_course(self)
                    elif student_operation == '4':
                        # 4、查看已选课程
                        Student.search_selected_course(self)
                    elif student_operation == '5':
                        # 5、退出学生选课（需总学分不得少于60）
                        break
                    elif student_operation in {'q', 'Q'}:
                        exit()  # 退出整个系统（程序）
                    else:
                        print("【亲爱的同学】你的输入有误，请重新输入！！！")

            # 2.管理员登录
            elif user == '2':
                Admin.admin_login(self)  # 管理员登录验证
                while True:
                    Menu.admin_operate_menu(self)  # 显示管理员操作菜单（二级菜单）
                    admin_operation = input("【尊敬的管理员】请输入你的操作：")
                    if admin_operation == '1':
                        # 1、课程信息录入
                        Admin.add_course(self)
                    elif admin_operation == '2':
                        # 2、课程信息浏览
                        Admin.show_all_courses(self)
                    elif admin_operation == '3':
                        # 3、查询某一学生选课信息（学生id查找）
                        Admin.search_someone_sc(self)
                    elif admin_operation == '4':
                        # 4、查看所有学生选课信息
                        Admin.search_all_sc(self)
                    elif admin_operation == '5':
                        # 5、退出管理员操作
                        break
                    elif admin_operation in {'q', 'Q'}:
                        exit()
                    else:
                        print("【尊敬的管理员】你的输入有误，请重新输入！！！")
            # 退出整个系统（程序）
            elif user in {'q', 'Q'}:
                exit()
            # 错误提示信息
            else:
                print("你的输入有误，请重新输入！！！")
