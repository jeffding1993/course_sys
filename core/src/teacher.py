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
    char = login_teacher_dic["teacher_name"] + " 教授的课程有 :\n"
    for course in login_teacher_dic["teacher_courses"]:
        char += (course + "\n")

    print(char)


@login_auth("teacher")
def choose_course():
    while 1:
        course_name = input("需要额外教授的课程：").strip()

        res, msg = teacher_interface.add_teacher_course(course_name, login_teacher_dic)

        if res:
            print(msg)
            login_teacher_dic["teacher_courses"].append(course_name)  # 更新登录信息
            res, msg = teacher_interface.save_teacher(login_teacher_dic)
            if res:
                return
        else:
            print(msg)


@login_auth("teacher")
def check_student(course_name=None):
    if not course_name:
        course_name = input("请输入需要查询学生的课程名称：").strip()
    teacher_dic = teacher_interface.select_teacher(login_teacher_dic["teacher_name"])
    if course_name in teacher_dic["teacher_courses"]:
        msg, course_dic = common_interface.choose_course(course_name)
        if course_dic:
            char = "有学生：\n"
            for student in course_dic["course_students"]:
                char += (student + "\n")
            print(char)
            return True
        else:
            print(msg)
            return False
    else:
        print("不教授此课程")


@login_auth("teacher")
def modify_score():  # 修改学生成绩     1.选择课程   2.打印课程下的学生  3.选择学生  输入成绩 修改字典的值
    while 1:
        check_course()
        course_name = input("请输入需要修改学生成绩的课程名称：").strip()
        if course_name not in login_teacher_dic["teacher_courses"]:
            print("错误输入")
            continue
        check_student(course_name=course_name)
        student_name = input("请输入需要修改学生成绩的学生名称：").strip()
        msg, course_dic = common_interface.choose_course(course_name)
        if student_name not in course_dic["course_students"]:
            print("无此学生，请重新输入")
            continue
        student_dic = student_interface.select_student(student_name)
        score = input("请输入该课程的成绩：").strip()
        student_dic["score"][course_name] = int(score)
        student_interface.save_student(student_dic)
        print("修改学生：%s 成绩成功, 成绩为 %s" % (student_name, score))
        return


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
