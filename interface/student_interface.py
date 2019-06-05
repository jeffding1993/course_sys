from db.models import Student


def student_register(username, password):
    stu_obj = Student.select(username)
    if stu_obj:
        return False, "学生已存在"

    Student(username, password)

    return True, "学生%s注册成功" % username
