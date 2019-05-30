from db import db_handler


def register(username, password):
    admin_dic = {"username": username,
                 "password": password
                 }
    print(admin_dic)
    res, msg = db_handler.save(admin_dic)

    if not res:
        print(msg)
        return res
    else:
        print(msg)
        return res
