from db.models import Admin, School, Teacher, Course


def register(username, password):
    admin_obj = Admin.select(username)

    if admin_obj:
        return False, "用户已存在"

    Admin(username, password)
    return True, "管理员注册成功"


def login(username, password):
    admin_obj = Admin.select(username)

    if not admin_obj:
        return False, "管理员账户不存在，请重新登录"

    if password == admin_obj.password:
        return True, "登录成功"
    else:
        return False, "密码错误，请重新输入"


def create_school(*args, **kwargs):
    # school_dic = {"school_name": args[0],
    #               "address": args[1],
    #               "teachers": [args[2]],
    #               "courses": [args[3]]
    #               }

    school_obj = School.select(args[0])
    if not school_obj:
        admin_obj = Admin.select(kwargs["admin_dic"]["username"])

        admin_obj.add_school(*args)

        return True, '%s 学校创建成功!' % args[0]
    else:
        return False, "此学校已存在"


def create_teacher(*args, **kwargs):
    # teacher_dic = {"teacher_name": args[0],
    #                "teacher_password": args[1],
    #                "teacher_school": args[2],
    #                "teacher_courses": [args[3]]
    #                }

    teacher_obj = Teacher.select(args[0])
    if teacher_obj:
        return False, "老师已存在"

    school_obj = School.select(args[2])
    if not school_obj:
        return False, "学校不存在"

    # 增加school对应的老师,如果不存在添加
    # if teacher_dic["teacher_name"] not in school_dic["teachers"]:
    #     school_dic["teachers"].append(teacher_dic["teacher_name"])
    if args[0] not in school_obj.teachers:
        school_obj.teachers.append(args[0])

    # 如果老师教授的课程学校没有，进行添加
    # for course in teacher_dic["teacher_courses"]:
    #     if course not in school_dic["courses"]:
    #         school_dic["courses"].append(course)


    # if args[3] not in school_obj.courses:
    #     school_obj.courses.append(args[3])
    # school_obj.save()

    # 创建老师信息
    admin_obj = Admin.select(kwargs["admin_dic"]["username"])
    if admin_obj:
        admin_obj.add_teacher(*args)

    return True, "老师创建成功"


def create_course(*args,**kwargs):
    # course_dic = {"school_name": args[0],
    #               "course_name": args[1],
    #               "course_price": int(args[2]),
    #               "course_period": args[3],
    #               "course_students": []
    #               }

    # 获取对应学校信息
    school_obj = School.select(args[0])

    if not school_obj:  # 判断学校是否存在
        return False, "学校不存在，请先创建学校"

    # 在学校课程信息里添加课程
    # if course_dic["course_name"] not in school_dic["courses"]:
    #     school_dic["courses"].append(course_dic["course_name"])
    #     db_handler.save_school(school_dic)
    # else:
    #     return False, "课程已存在，无需添加"

    admin_obj = Admin.select(kwargs["admin_dic"]["username"])
    if not admin_obj:
        return False, "管理员不存在"

    if args[1] not in school_obj.courses:
        school_obj.courses.append(args[1])
        school_obj.save()

    admin_obj.add_course(*args)

    return True, "课程已创建"
