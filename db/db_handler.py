from db.models import PickleDb
from conf import settings
import os


def save(user_dic):
    # 判断admin存放目录是否存在，不存在则创建
    if not os.path.exists(settings.ADMIN_DIR):
        os.mkdir(settings.ADMIN_DIR)

    # 目标存放位置
    file_path = os.path.join(settings.ADMIN_DIR, "%s.pic" % user_dic["username"])

    if os.path.exists(file_path):
        return False, "用户已存在, 请重新输入"

    # 使用pickle存放
    target = PickleDb(user_dic, file_path)
    target.save()
    return True, "管理员注册成功"
