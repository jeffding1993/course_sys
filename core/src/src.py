from core.src import admin, student, teacher

view_map = {
    "1": student,
    "2": teacher,
    "3": admin
}


def run():
    while 1:
        choice = input('''
        1：学生登录
        2：老师登录
        3：管理登录
        （输入q退出）''')
        if choice == "q":
            print("已退出")
            break
        if choice in view_map:
            view_map[choice]
        else:
            print("错误输入，请重输")
