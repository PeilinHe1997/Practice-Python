 # 学生管理系统

'''
增加学员
删除学员
修改学员
查找学员
'''
stu1 = {"name":"Tom","age":19,"gender":"Male","height":180}
stu2 = {"name":"Riddle","age":25,"gender":"Female","height":168}
stu3 = {"name":"Harry","age":23,"gender":"Male","height":175}
stu4 = {"name":"Lily","age":22,"gender":"Female","height":173}
students = [stu1,stu2,stu3,stu4]
while True:
    print("\n\n-----------学生管理系统-------------\n\n")
    print("1.增加学生\n2.删除学生\n3.修改学生\n4.查找学生\n5.退出程序")
    num = int(input("请输入您要操作的编号："))
    if num ==1:
        #让用户输入信息
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄"))
        gender = input("请输入学生性别")
        height = int(input("请输入学生身高"))
        #将学生信息添加到新的字典中
        stu5 = {"name":name,"age":age,"gender":gender,"height":height}
        students.append(stu5)
        #刷新学生信息（遍历学生信息）
        for stu in students:
            print("----------------------")
            for key, value in stu.items():
                print(key, value)



    elif num ==2:
        #删除学生
        print("1.按编号删除\n2.全部删除")
        choose = int(input("请选择您要进行的操作："))
        if choose ==1:
            stu_num = int(input("请您输入需要删除学生的编号"))
            students.pop(stu_num-1)
            print("该学生已经被删除")
           #刷新学生信息（遍历学生信息）
            for stu in students:
                print("----------------------")
                for key, value in stu.items():
                    print(key, value)
        if choose ==2:
            yes_no = input("确定要全部清空吗？yes/no")
            if yes_no == "yes":
                students.clear()
                print("已清空所有数据")
        else:
            print("选择有误")



            
    elif num ==3:
        #修改学生信息
        print("当前有"+str(len(students))+"个学生")
        stu_number = int(input("请输入要修改学生的编号："))
        students.pop(stu_number-1)
        #让用户输入信息
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄"))
        gender = input("请输入学生性别")
        height = int(input("请输入学生身高"))
        #将学生信息添加到新的字典中
        stu5 = {"name":name,"age":age,"gender":gender,"height":height}
        students.insert(stu_number-1,stu5)
        #刷新学生信息（遍历学生信息）
        for stu in students:
            print("----------------------")
            for key, value in stu.items():
                print(key, value)


                
    elif num ==4:
        #查找学生信息
        print("当前有"+str(len(students))+"个学生")
        #刷新学生信息（遍历学生信息）
        stu_number = int(input("请输入要查找学生的编号："))
        for key, value in students[stu_number-1].items():
            print(key, value)



    elif num ==5:
        yes_no = input("您确定要退出吗？ yes/no")
        if yes_no == "yes":
            print("程序已关闭！欢迎下次再来")
            break


    else:
        print("您输入有误，请重新输入")
    
