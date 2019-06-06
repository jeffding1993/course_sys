from db.models import Course


def choose_course(student_name, course_name):
    '''
    课程添加学生
    :param course_name:
    :param student_name:
    :return:
    '''
    course_obj = Course.select(course_name)

    course_obj.add_student(student_name)

    return True
