from interface import admin_interface, common_interface
from lib.common import login_auth

login_admin_dic = {}


def admin_register():
    while 1:
        name = input("请输入管理员用户名：").strip()
        password = input("请输入对应的密码：").strip()
        again_password = input("请输入同样的密码：").strip()
        if again_password == password:
            res, msg = admin_interface.register(name, again_password)
            if res:
                print(msg)
                return
            else:
                print(msg)
        else:
            print("密码不同，请重新注册")


def admin_login():
    while 1:
        name = input("请输入需要登录的管理员用户名：").strip()
        password = input("请输入密码：").strip()
        res, msg = common_interface.login_interface(name, password, "admin")

        if res:
            print(msg)
            login_admin_dic["username"] = name
            login_admin_dic["password"] = password
            return
        else:
            print(msg)


@login_auth("admin")
def admin_create_school():
    while 1:
        # 学校  学校的名字 地址  老师 课程
        school_name = input("输入需要创建的学校名称：").strip()
        address = input("输入学校所在的地址：").strip()

        res, msg = admin_interface.create_school(school_name, address, admin_dic=login_admin_dic)

        if res:
            print(msg)
            return
        else:
            print(msg)


@login_auth("admin")
def admin_create_teacher():
    # 老师  姓名  密码   教授的课程
    teacher_name = input("请输入老师的名称：").strip()
    teacher_password = input("请输入老师的密码：").strip()
    teacher_school = input("请输入老师所在的学校：").strip()
    # teacher_course = input("请输入老师教授的课程：").strip()

    res, msg = admin_interface.create_teacher(teacher_name, teacher_password, teacher_school, admin_dic=login_admin_dic)

    if res:
        print(msg)
        return
    else:
        print(msg)


@login_auth("admin")
def create_course():
    # 课程 名称 价格 周期  学生
    while 1:
        school_list = common_interface.select_all_file("school")
        if not school_list:
            print("无学校可选择，请先创建学校。")
            return

        for i, v in enumerate(school_list):
            print(i, v)
        school_num = input("请输入需要需要添加课程的学校序号：").strip()
        if school_num.isdigit():
            school_num = int(school_num)

            if school_num >= 0 and school_num < len(school_list):
                school_name = school_list[school_num]
                course_name = input("请输入对应的课程名称：").strip()
                course_price = input("请输入课程的价格：").strip()
                course_period = input("请输入课程的周期：").strip()
                # 课程信息存储
                res, msg = admin_interface.create_course(school_name, course_name, course_price, course_period,
                                                         admin_dic=login_admin_dic)
                if res:
                    print(msg)
                    return
                else:
                    print(msg)
            else:
                print("输入学校编号错误，请重新输入。")


func_map = {
    "1": admin_register,
    "2": admin_login,
    "3": admin_create_school,
    "4": admin_create_teacher,
    "5": create_course
}


def run():
    while 1:
        choice = input('''
1. 管理员注册
2. 管理员登录
3. 创建学校
4. 创建老师
5. 创建课程
（输入q退出）
>>> ''')
        if choice == "q":
            print("返回主界面")
            break
        if choice in func_map:
            func_map[choice]()
        else:
            print("错误输入，请重输")
