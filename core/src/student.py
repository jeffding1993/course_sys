def student_register():
    pass


def student_login():
    pass


def choose_school():
    pass


def choose_course():
    pass


def check_score():
    pass


func_map = {
    "1": student_register,
    "2": student_login,
    "3": choose_school,
    "4": choose_course,
    "5": check_score
}


def run():
    while 1:
        choice = input('''
1. 学生注册
2. 学生登录
3. 选择校区
4. 选择课程
5. 查看成绩
（输入q退出）
>>> ''')
        if choice == "q":
            print("返回主界面")
            break
        if choice in func_map:
            func_map[choice]()
        else:
            print("错误输入，请重输")
