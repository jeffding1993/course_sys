def teacher_login():
    pass


def check_course():
    pass


def choose_course():
    pass


def check_student():
    pass


def modify_score():
    pass


func_map = {
    "1": teacher_login,
    "2": check_course,
    "3": choose_course,
    "4": check_student,
    "5": modify_score
}


def run():
    while 1:
        choice = input('''
1. 老师登录
2. 查看教授课程
3. 选择教授课程
4. 查看课程下学生
5. 修改学生成绩
（输入q退出）
>>> ''')
        if choice == "q":
            print("返回主界面")
            break
        if choice in func_map:
            func_map[choice]()
        else:
            print("错误输入，请重输")
