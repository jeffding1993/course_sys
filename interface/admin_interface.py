from db import db_handler


def register(username, password):
    admin_dic = {"username": username,
                 "password": password
                 }

    res = db_handler.admin_save(admin_dic)

    if not res:
        return res, "用户已存在, 请重新输入"
    else:
        return res, "管理员注册成功"


def login(username, password):
    admin_dic = {"username": username,
                 "password": password
                 }
    res, user_dic = db_handler.admin_select(admin_dic)

    if not res:
        return False, "管理员账户不存在，请重新登录"

    if password == user_dic["password"]:
        return True, "登录成功"
    else:
        return False, "密码错误，请重新输入"


def create_school(*args):
    school_dic = {"school_name": args[0],
                  "address": args[1],
                  "teachers": [args[2]],
                  "courses": [args[3]]
                  }

    res = db_handler.create_school(school_dic)

    if not res:
        return res, "学校已存在, 请重新输入"
    else:
        return res, "学校创建成功"


def create_teacher(*args):
    teacher_dic = {"teacher_name": args[0],
                   "teacher_password": args[1],
                   "teacher_school": args[2],
                   "teacher_courses": [args[3]]
                   }

    res, school_dic = db_handler.select_school(teacher_dic["teacher_school"])

    if not res:  # 判断老师所在的学校是否存在
        return False, "学校不存在，请先创建学校"

    # 增加school对应的老师,如果不存在添加
    if teacher_dic["teacher_name"] not in school_dic["teachers"]:
        school_dic["teachers"].append(teacher_dic["teacher_name"])

    # 如果老师教授的课程学校没有，进行添加
    for course in teacher_dic["teacher_courses"]:
        if course not in school_dic["courses"]:
            school_dic["courses"].append(course)

    # 创建老师信息
    res = db_handler.create_teacher(teacher_dic)

    if not res:
        return res, "老师已存在, 请重新输入"
    else:
        db_handler.save_school(school_dic)
        return res, "老师创建成功"


def add_course(school_name, course_name):
    # 获取对应学校信息
    res, school_dic = db_handler.select_school(school_name)

    if not res:  # 判断学校是否存在
        return False, "学校不存在，请先创建学校"

    if course_name not in school_dic["courses"]:
        school_dic["courses"].append(course_name)
        db_handler.save_school(school_dic)
        return True, "添加课程成功"
    else:
        return False, "课程已存在，无需添加"
