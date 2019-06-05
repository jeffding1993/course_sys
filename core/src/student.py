from interface import student_interface, school_interface, common_interface
from lib.common import login_auth

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


@login_auth("student")
def choose_school():
    school_name = input("请输入校区：").strip()

    res, msg = school_interface.choose_school(school_name)

    if res:
        print(msg)
        login_student_dic["school_name"] = school_name
        student_interface.save_student(login_student_dic)
    else:
        print(msg)


@login_auth("student")
def choose_course():
    course_name = input("请输入课程：").strip()

    res = school_interface.choose_course(login_student_dic)

    if (course_name in res) and (course_name not in login_student_dic["courses"]):
        # 课程信息添加学生
        msg, course_dic = common_interface.choose_course(course_name)
        if course_dic:
            print(msg)
            course_dic["course_students"].append(login_student_dic["student_name"])
            common_interface.save_course(course_dic)
        else:
            print(msg)
            return False
        login_student_dic["courses"].append(course_name)
        student_interface.save_student(login_student_dic)
        print("课程选择成功")
    else:
        print("选课失败")


@login_auth("student")
def check_score():
    char = "现有的课程如下：\n"
    for course in login_student_dic["courses"]:
        char += course
    print(char)
    course_name = input("请输入需要查看成绩的课程名称：").strip()
    if course_name not in login_student_dic["courses"]:
        print("错误输入")
        return False
    print("课程%s ：的成绩为 %s" % (course_name, login_student_dic["score"][course_name]))


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
