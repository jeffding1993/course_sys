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

        res, msg = common_interface.login_interface(student_name, student_password, "student")

        if res:
            print(msg)
            login_student_dic["username"] = student_name
            return
        else:
            print(msg)


@login_auth("student")
def choose_school():
    while 1:
        school_list = student_interface.get_school_list("school")
        if not school_list:
            return False, "没有创建学校，请先创建"

        for i, v in enumerate(school_list):
            print(i, v)

        choice = input("请输入校区编号（输入q退出）：").strip()

        if choice == "q":
            print("退出")
            break

        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(school_list):
                res, msg = student_interface.choose_school(login_student_dic["username"], school_list[choice])
                if res:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print("非法输入，请重新输入")
        else:
            print("输入非数字，请重新输入")


@login_auth("student")
def choose_course():
    while 1:

        res, msg = student_interface.check_school(login_student_dic["username"])

        if not res:
            print(msg)
            break

        courses_list = student_interface.get_courses_list(login_student_dic["username"])

        if not courses_list:
            print("学校无课程，请先创建课程")
            break

        for i, v in enumerate(courses_list):
            print(i, v)

        choice = input("请输入课程编号：").strip()

        if choice.isdigit():
            choice = int(choice)
            if len(courses_list) > choice >= 0:
                res, msg = student_interface.choose_course(login_student_dic["username"], courses_list[choice])

                if res:
                    res = school_interface.choose_course(login_student_dic["username"], courses_list[choice])
                    if res:
                        print(msg)
                        break
                    else:
                        print("课程信息修改错误")
                else:
                    print(msg)
            else:
                print("请输入正确编号")
        else:
            print("请输入数字")


@login_auth("student")
def check_score():
    res = student_interface.check_score(login_student_dic["username"])

    if not res:
        print("学生%s 还没有课程成绩" % login_student_dic["username"])
        return

    for k, v in res.items():
        print(k + " 成绩为：" + v)


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
