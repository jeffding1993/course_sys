def admin_auth(func):
    from core.src import admin

    def inner(*args, **kwargs):
        if admin.login_admin_dic:
            res = func(*args, **kwargs)
            return res
        else:
            admin.admin_login()

    return inner


def teacher_auth(func):
    from core.src import teacher

    def inner(*args, **kwargs):
        if teacher.login_teacher_dic:
            res = func(*args, **kwargs)
            return res
        else:
            teacher.teacher_login()

    return inner


def student_auth(func):
    from core.src import student

    def inner(*args, **kwargs):
        if student.login_student_dic:
            res = func(*args, **kwargs)
            return res
        else:
            student.student_login()

    return inner
