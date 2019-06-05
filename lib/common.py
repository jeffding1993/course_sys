def login_auth(user_type):
    def auth(func):
        from core.src import admin, teacher, student

        def inner(*args, **kwargs):

            if user_type == "admin":
                if admin.login_admin_dic:
                    return func(*args, **kwargs)
                else:
                    admin.admin_login()
            if user_type == "teacher":
                if teacher.login_teacher_dic:
                    return func(*args, **kwargs)
                else:
                    teacher.teacher_login()
            if user_type == "student":
                if student.login_student_dic:
                    return func(*args, **kwargs)
                else:
                    student.student_login()

        return inner

    return auth
