from db import db_handler


def teacher_login(teacher_name, teacher_password):
    res, teacher_dic = db_handler.select_teacher({"teacher_name": teacher_name, "teacher_password": teacher_password})

    if not res:
        return False, "无此老师，请重新登录。"

    if teacher_password == teacher_dic["teacher_password"]:
        return True, "老师登录成功"
    else:
        return False, "密码错误，请重新登录"


def select_teacher(teacher_name):
    res, teacher_dic = db_handler.select_teacher({"teacher_name": teacher_name})

    return teacher_dic


def add_teacher_course(course_name, login_teacher_dic):
    res, teacher_dic = db_handler.select_teacher(login_teacher_dic)

    if course_name not in teacher_dic["teacher_courses"]:
        teacher_dic["teacher_courses"].append(course_name)
        db_handler.save_teacher(teacher_dic)

        # 学校课程信息更新
        res, school_dic = db_handler.select_school(teacher_dic["teacher_school"])
        school_dic["courses"].append(course_name)
        db_handler.save_school(school_dic)

        return True, "老师可教授课程添加成功"
    else:
        return False, "课程已存在"


def save_teacher(teacher_dic):
    res = db_handler.save_teacher(teacher_dic)

    if res:
        return True, "老师信息保存成功"
    else:
        return False, "老师信息保存失败"
