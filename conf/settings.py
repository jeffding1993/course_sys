import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "db")
ADMIN_DIR = os.path.join(DB_PATH, "admin")
STUDENT_DIR = os.path.join(DB_PATH, "student")
TEACHER_DIR = os.path.join(DB_PATH, "teacher")
COURSE_DIR = os.path.join(DB_PATH, "course")
