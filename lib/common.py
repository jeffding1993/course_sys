
def admin_auth(func):
    from core.src import admin

    def inner(*args, **kwargs):
        if admin.login_admin_dic:
            res = func(*args, **kwargs)
            return res
        else:
            admin.admin_login()

    return inner
