from interface.admin_interface import register, login, create_school
from lib.common import admin_auth

login_admin_dic = {}


def admin_register():
    while 1:
        name = input("请输入管理员用户名：").strip()
        password = input("请输入对应的密码：").strip()
        again_password = input("请输入同样的密码：").strip()
        if again_password == password:
            res, msg = register(name, again_password)
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
        res, msg = login(name, password)

        if res:
            print(msg)
            login_admin_dic["username"] = name
            login_admin_dic["password"] = password
            return
        else:
            print(msg)


@admin_auth
def admin_create_school():
    while 1:
        # 学校  学校的名字 地址  老师 课程
        school_name = input("输入需要创建的学校名称：").strip()
        address = input("输入学校所在的地址：").strip()
        teacher = input("输入学校老师（创校老师）名称：").strip()
        course = input("所教授的课程：").strip()

        res, msg = create_school(school_name, address, teacher, course)

        if res:
            print(msg)
            return
        else:
            print(msg)


def create_teacher():
    pass


def create_course():
    pass


func_map = {
    "1": admin_register,
    "2": admin_login,
    "3": admin_create_school,
    "4": create_teacher,
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
