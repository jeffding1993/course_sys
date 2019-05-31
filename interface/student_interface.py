from db import db_handler


def student_register(username, password):
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


def student_login(student_name, student_password):
    student_dic = {"username": student_name,
                   "password": student_password
                   }

    res, user_dic = db_handler.select_student(student_dic["username"])

    if not res:
        return False, "学生账户不存在，请重新登录"

    if student_password == student_dic["password"]:
        return True, "登录成功"
    else:
        return False, "密码错误，请重新输入"
