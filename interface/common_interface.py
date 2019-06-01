from db import db_handler


def choose_course(course_name):
    res, course_dic = db_handler.select_course(course_name)

    if not res:
        return "无此课程", {}
    return "课程信息存在", course_dic
