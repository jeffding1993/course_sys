import pickle
from conf import settings
import os


def db_save(obj):
    path = os.path.join(settings.DB_PATH, obj.__class__.__name__.lower())

    if not os.path.isdir(path):  # 不存在则创建目录
        os.mkdir(path)

    file_path = os.path.join(path, obj.name)

    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()


def db_select(cls, name):
    path = os.path.join(settings.DB_PATH, cls.__name__.lower())

    user_path = os.path.join(path, name)

    if not os.path.exists(user_path):

        return False

    with open(user_path, 'rb') as f:
        user_obj = pickle.load(f)
        if user_obj:
            return user_obj
        else:
            return False
