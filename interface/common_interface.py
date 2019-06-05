import os
from conf import settings


# 查看文件
def select_all_file(name):
    file_path = os.path.join(settings.DB_PATH, name)

    if not os.path.exists(file_path):
        return False
    return os.listdir(file_path)
