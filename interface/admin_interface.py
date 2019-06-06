from db.models import Admin, School, Teacher


def register(username, password):
    admin_obj = Admin.select(username)

    if admin_obj:
        return False, "用户已存在"

    Admin(username, password)
    return True, "管理员注册成功"


def create_school(*args, **kwargs):
    school_obj = School.select(args[0])
    if not school_obj:
        admin_obj = Admin.select(kwargs["admin_dic"]["username"])
        if admin_obj:
            admin_obj.add_school(*args)

        return True, '%s 学校创建成功!' % args[0]
    else:
        return False, "此学校已存在"


def create_teacher(*args, **kwargs):
    teacher_obj = Teacher.select(args[0])
    if teacher_obj:
        return False, "老师已存在"

    school_obj = School.select(args[2])
    if not school_obj:
        return False, "学校不存在"

    if args[0] not in school_obj.teachers:
        school_obj.add_teacher(args[0])

    # 创建老师信息
    admin_obj = Admin.select(kwargs["admin_dic"]["username"])
    if admin_obj:
        admin_obj.add_teacher(*args)

    return True, "老师创建成功"


def create_course(*args, **kwargs):
    # 获取对应学校信息
    school_obj = School.select(args[0])

    if not school_obj:  # 判断学校是否存在
        return False, "学校不存在，请先创建学校"

    admin_obj = Admin.select(kwargs["admin_dic"]["username"])
    if not admin_obj:
        return False, "管理员不存在"

    if args[1] not in school_obj.courses:
        school_obj.add_course(args[1])
        school_obj.save()

    admin_obj.add_course(*args)

    return True, "课程已创建"
