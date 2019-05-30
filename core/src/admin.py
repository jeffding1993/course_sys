def admin_register():
    pass


def admin_login():
    pass


def create_school():
    pass


def create_teacher():
    pass


def create_course():
    pass


func_map = {
    "1": admin_register,
    "2": admin_login,
    "3": create_school,
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
