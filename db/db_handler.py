from db.models import PickleDb
from conf import settings
import os


def admin_save(user_dic):
    # 判断admin存放目录是否存在，不存在则创建
    if not os.path.exists(settings.ADMIN_DIR):
        os.mkdir(settings.ADMIN_DIR)

    # 目标存放位置
    file_path = os.path.join(settings.ADMIN_DIR, "%s.pic" % user_dic["username"])

    # 判断用户是否存在
    if os.path.exists(file_path):
        return False

    # 使用pickle存放
    target = PickleDb(user_dic, file_path)
    target.save()
    return True


def admin_select(admin_dic):
    # 目标存放位置
    file_path = os.path.join(settings.ADMIN_DIR, "%s.pic" % admin_dic["username"])

    if not os.path.exists(file_path):
        return False, {}

    target = PickleDb(admin_dic, file_path)
    return True, target.select()


def create_school(school_dic):
    # 判断school存放目录是否存在，不存在则创建
    if not os.path.exists(settings.SCHOOL_DIR):
        os.mkdir(settings.SCHOOL_DIR)

    # 学校存放位置
    file_path = os.path.join(settings.SCHOOL_DIR, "%s.pic" % school_dic["school_name"])

    # 判断学校是否存在
    if os.path.exists(file_path):
        return False

    # 使用pickle存放
    target = PickleDb(school_dic, file_path)
    target.save()
    return True
