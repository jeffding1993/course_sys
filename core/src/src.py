from core.src import admin, student, teacher

view_map = {
    "1": student,
    "2": teacher,
    "3": admin
}


def run():
    while 1:
        choice = input('''
1：学生视图
2：老师视图
3：管理视图
（输入q退出）
>>> ''')
        if choice == "q":
            print("已退出,结束程序")
            break
        if choice in view_map:
            view_map[choice].run()
        else:
            print("错误输入，请重输")
