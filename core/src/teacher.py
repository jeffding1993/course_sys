from interface import teacher_interface, common_interface, student_interface
from lib.common import login_auth

login_teacher_dic = {}


def teacher_login():
    while 1:
        teacher_name = input("请输入老师的名称：").strip()
        teacher_password = input("请输入老师的密码：").strip()

        res, msg = common_interface.login_interface(teacher_name, teacher_password, "teacher")

        if res:
            print(msg)
            login_teacher_dic["username"] = teacher_name
            return
        else:
            print(msg)


@login_auth("teacher")
def check_course():
    char = login_teacher_dic["username"] + " 教授的课程有 :\n"
    res = teacher_interface.get_teacher_courses(login_teacher_dic["username"])

    if not res:
        print("老师还没有选择教授的课程，请先选择")
        return

    for i, v in enumerate(res):
        char += v + "\n"
    print(char)


@login_auth("teacher")
def choose_course():
    while 1:
        course_list = common_interface.select_all_file("course")
        if not course_list:
            print("无课程，请先创建")

        for i, v in enumerate(course_list):
            print(i, v)

        choice = input("需要额外教授的课程编号：").strip()

        if choice.isdigit():
            choice = int(choice)

            if len(course_list) > choice >= 0:
                res, msg = teacher_interface.add_teacher_course(login_teacher_dic["username"], course_list[choice])

                if res:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print("请输入正确的编号")
        else:
            print("请输入数字")


@login_auth("teacher")
def check_student():
    while 1:
        teacher_course_list = teacher_interface.get_teacher_courses(login_teacher_dic["username"])

        if not teacher_course_list:
            print("老师还未选择课程")
            break

        for i, v in enumerate(teacher_course_list):
            print(i, v)

        choice = input("选择需要查看学生的课程编号：").strip()

        if choice.isdigit():
            choice = int(choice)

            if len(teacher_course_list) > choice >= 0:
                res, msg = teacher_interface.check_student(teacher_course_list[choice])

                if not res:
                    print(msg)
                    break

                print("课程学生有：")
                for v in res:
                    print(v + "\n")
                break
            else:
                print("请输入正确编号")
        else:
            print("请输入数字")


@login_auth("teacher")
def modify_score():  # 修改学生成绩     1.选择课程   2.打印课程下的学生  3.选择学生  输入成绩 修改字典的值
    while 1:
        course_list = teacher_interface.get_teacher_courses(login_teacher_dic["username"])

        if not course_list:
            print("老师没有选择课程课程")

        for i, v in enumerate(course_list):
            print(i, v)

        choice = input("选择需要修改学生成绩的课程编号：").strip()

        if choice.isdigit():
            choice = int(choice)
            course_name = course_list[choice]

            if len(course_list) > choice >= 0:
                res, msg = teacher_interface.check_student(course_list[choice])

                if not res:
                    print(msg)
                    break

                for i, v in enumerate(res):
                    print(i, v)

                choice = input("选择学生编号：").strip()

                if choice.isdigit():
                    choice = int(choice)

                    if len(res) > choice >= 0:
                        student_name = res[choice]
                        score = input("请输入成绩：")
                        res, msg = teacher_interface.modify_student_score(course_name, student_name, int(score))
                        if res:
                            print(msg)
                            break
                    else:
                        print("请输入正确选项")
                else:
                    print("请输入数字")
            else:
                print("请输入正确选项")
        else:
            print("请输入数字")


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
3. 添加教授课程
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
