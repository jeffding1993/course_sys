from db import db_handler


def register(username, password):
    admin_dic = {"username": username,
                 "password": password}

    res = db_handler.admin_save(admin_dic)

    if not res:
        return res, "用户已存在, 请重新输入"
    else:
        return res, "管理员注册成功"


def login(username, password):
    admin_dic = {"username": username,
                 "password": password}
    res, user_dic = db_handler.admin_select(admin_dic)

    if not res:
        return False, "管理员账户不存在，请重新登录"

    if password == user_dic["password"]:
        return True, "登录成功"
    else:
        return False, "密码错误，请重新输入"
