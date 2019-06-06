from db.models import Student, School
from interface import common_interface


def student_register(username, password):
    stu_obj = Student.select(username)
    if stu_obj:
        return False, "学生已存在"

    Student(username, password)

    return True, "学生%s注册成功" % username


def get_school_list(name):
    return common_interface.select_all_file(name)


def choose_school(student_name, school_name):
    stu_obj = Student.select(student_name)

    if stu_obj.school_name:
        return False, "学生已选择过学校"

    stu_obj.choose_school(school_name)

    return True, "选择校区%s" % school_name


def get_courses_list(stu_name):
    stu_obj = Student.select(stu_name)
    school_obj = School.select(stu_obj.school_name)

    return school_obj.courses


def choose_course(student_name, course_name):
    stu_obj = Student.select(student_name)

    if course_name in stu_obj.courses:
        return False, "学生已选择过此课程"

    stu_obj.choose_course(course_name)

    return True, "选择课程%s成功" % course_name


def check_school(name):
    stu_obj = Student.select(name)
    if not stu_obj.school_name:
        return False, "学生还没有选择学校"
    return True, "学校已选择"


def check_score(name):
    stu_obj = Student.select(name)

    if not stu_obj.score:
        return False

    return stu_obj.score


