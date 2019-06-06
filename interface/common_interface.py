import os
from conf import settings
from db import models


# 查看文件
def select_all_file(name):
    file_path = os.path.join(settings.DB_PATH, name)

    if not os.path.exists(file_path):
        return False
    return os.listdir(file_path)


# 通用登录接口
def login_interface(user_name, password, user_type):
    if user_type == "student":
        obj = models.Student.select(user_name)

        if not obj:
            return False, "学员账户不存在"

    elif user_type == "admin":
        obj = models.Admin.select(user_name)

        if not obj:
            return False, "管理员账户不存在"

    elif user_type == "teacher":
        obj = models.Teacher.select(user_name)

        if not obj:
            return False, "老师账户不存在"
    else:
        return False, "没有此权限"

    if password == obj.password:
        return True, "登录成功"
    else:
        return False, "密码错误，请重新输入"
