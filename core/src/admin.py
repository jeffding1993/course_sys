from interface.admin_interface import register

def admin_register():
    while 1:
        name = input("请输入管理员用户名：").strip()
        password = input("请输入对应的密码：").strip()
        again_password = input("请输入同样的密码：").strip()
        if again_password == password:
            res = register(name, again_password)
            if res:
                return



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
