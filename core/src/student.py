from interface import student_interface, school_interface
from lib.common import student_auth

login_student_dic = {}


def student_register():
    while 1:
        name = input("请输入学生用户名：").strip()
        password = input("请输入对应的密码：").strip()
        again_password = input("请输入同样的密码：").strip()
        if again_password == password:
            res, msg = student_interface.student_register(name, again_password)
            if res:
                print(msg)
                return
            else:
                print(msg)
        else:
            print("密码不同，请重新注册")


def student_login():
    while 1:
        student_name = input("请输入学生的名称：").strip()
        student_password = input("请输入学生的密码：").strip()

        res, msg = student_interface.student_login(student_name, student_password)

        if res:
            print(msg)
            global login_student_dic
            login_student_dic = student_interface.select_student(student_name)
            return
        else:
            print(msg)


@student_auth
def choose_school():
    school_name = input("请输入校区：").strip()

    res, msg = school_interface.choose_school(school_name)

    if res:
        print(msg)
        login_student_dic["school_name"] = school_name
        student_interface.save_student(login_student_dic)
    else:
        print(msg)


@student_auth
def choose_course():
    course_name = input("请输入课程：").strip()

    res = school_interface.choose_course(login_student_dic)

    if (course_name in res) and (course_name not in login_student_dic["courses"]):
        login_student_dic["courses"].append(course_name)
        student_interface.save_student(login_student_dic)
        print("课程选择成功")
        print(login_student_dic)
    else:
        print("选课失败")


@student_auth
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
