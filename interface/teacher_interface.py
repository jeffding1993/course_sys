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
