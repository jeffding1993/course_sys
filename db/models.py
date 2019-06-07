from db import db_handler


class Base(object):

    def save(self):
        db_handler.db_save(self)

    @classmethod
    def select(cls, name):
        obj = db_handler.db_select(cls, name)
        return obj


class Admin(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    @classmethod
    def add_school(cls, *args):
        School(*args)

    @staticmethod
    def add_teacher(*args):
        Teacher(*args)

    @staticmethod
    def add_course(*args):
        Course(*args)


class School(Base):
    def __init__(self, school_name, address):
        self.name = school_name
        self.address = address
        self.teachers = []
        self.courses = []
        self.save()

    def add_course(self, course_name):
        self.courses.append(course_name)
        self.save()

    def add_teacher(self, teacher_name):
        self.teachers.append(teacher_name)
        self.save()


class Teacher(Base):
    def __init__(self, *args):
        self.name = args[0]
        self.password = args[1]
        self.courses = []
        self.save()

    def add_course(self, course_name):
        self.courses.append(course_name)
        self.save()

    @staticmethod
    def modify_student_score(stu_obj, course_name, score):
        stu_obj.score[course_name] = score
        stu_obj.save()


class Course(Base):
    def __init__(self, *args):
        self.school_name, self.name, self.price, self.period = args
        self.students = []
        self.save()

    def add_student(self, student_name):
        self.students.append(student_name)
        self.save()


class Student(Base):
    def __init__(self, *args):
        self.name, self.password = args
        self.courses = []
        self.school_name = None
        self.score = {}
        self.save()

    def choose_course(self, course_name):
        self.courses.append(course_name)
        self.save()

    def choose_school(self, schooL_name):
        self.school_name = schooL_name
        self.save()
