from db.models import Teacher, Course, Student


def get_teacher_courses(teacher_name):
    teacher_obj = Teacher.select(teacher_name)

    if not teacher_obj.courses:
        return False

    return teacher_obj.courses


def add_teacher_course(teacher_name, course_name):
    teacher_obj = Teacher.select(teacher_name)

    if course_name not in teacher_obj.courses:
        teacher_obj.add_course(course_name)

        return True, "老师选择课程成功"
    else:
        return False, "课程已被选择"


def check_student(course_name):
    course_obj = Course.select(course_name)

    if not course_obj:
        return False, "无此课程"
    elif not course_obj.students:
        return False, "课程无学生"

    return course_obj.students, "学生列表"


def modify_student_score(course_name, student_name, score: int):
    stu_obj = Student.select(student_name)

    Teacher.modify_student_score(stu_obj, course_name, score)

    return True, "修改%s的%s成绩为%s成功" % (student_name, course_name, str(score))
