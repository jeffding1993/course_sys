from db import db_handler


def register(username, password):
    student_dic = {"username": username,
                   "password": password,
                   "courses": [],
                   "school": '',
                   "score": {}
                   }

    res = db_handler.create_student(student_dic)

    if not res:
        return res, "用户已存在, 请重新输入"
    else:
        return res, "学生%s注册成功" % username
