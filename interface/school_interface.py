from db import db_handler


def create_course(*args):
    course_dic = {"school_name": args[0],
                  "course_name": args[1],
                  "course_price": int(args[2]),
                  "course_period": args[3],
                  "course_students": []
                  }

    # 获取对应学校信息
    res, school_dic = db_handler.select_school(course_dic["school_name"])

    if not res:  # 判断学校是否存在
        return False, "学校不存在，请先创建学校"

    if course_dic["course_name"] not in school_dic["courses"]:
        school_dic["courses"].append(course_dic["course_name"])
        db_handler.save_school(school_dic)
    else:
        return False, "课程已存在，无需添加"

    res = db_handler.create_course(course_dic)

    if not res:  # 判断课程是否存在
        return False, "课程已存在"
    return True, "课程已创建"


def choose_school(school_name):
    res, school_dic = db_handler.select_school(school_name)

    if not res:
        return False, "校区不存在"

    return True, "选择校区%s" % school_name


def choose_course(login_dic):
    res, school_dic = db_handler.select_school(login_dic["school_name"])

    return school_dic["courses"]
