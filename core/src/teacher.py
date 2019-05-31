from interface import teacher_interface
from lib.common import teacher_auth

login_teacher_dic = {}


def teacher_login():
    while 1:
        teacher_name = input("请输入老师的名称：").strip()
        teacher_password = input("请输入老师的密码：").strip()

        res, msg = teacher_interface.teacher_login(teacher_name, teacher_password)

        if res:
            print(msg)
            login_teacher_dic["teacher_name"] = teacher_name
            login_teacher_dic["teacher_courses"] = teacher_interface.select_teacher(teacher_name)["teacher_courses"]
            return
        else:
            print(msg)


@teacher_auth
def check_course():
    char = login_teacher_dic["teacher_name"] + " 教授的课程有 "
    for course in login_teacher_dic["teacher_courses"]:
        char += ("," + course)

    print(char)


@teacher_auth
def choose_course():
    while 1:
        course_name = input("需要教授的课程：").strip()

        res, msg = teacher_interface.add_teacher_course(course_name, login_teacher_dic)

        if res:
            print(msg)
            login_teacher_dic["teacher_courses"].append(course_name)  # 更新登录信息
            print(login_teacher_dic)
            return
        else:
            print(msg)


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
