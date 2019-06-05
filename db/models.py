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

    def add_teacher(self, *args):
        Teacher(*args)

    def add_course(self, *args):
        Course(*args)


class School(Base):
    def __init__(self, school_name, address):
        self.name = school_name
        self.address = address
        self.teachers = []
        self.courses = []
        self.save()


class Teacher(Base):
    def __init__(self, *args):
        self.name = args[0]
        self.password = args[1]
        self.courses = []
        self.save()


class Course(Base):
    def __init__(self, *args):
        self.school_name, self.name, self.price, self.period = args
        self.students = []
        self.save()
