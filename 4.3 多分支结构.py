# 多分支结构
'''
案例：如果你的成绩高于90，奖励一台笔记本电脑；
高于80，奖励一套Python学习教程；
高于70，奖励一支笔；
否则重做试卷

'''

#else 和 if 要对其
score = int(input("1.请输入您的成绩"))
if score >= 90:
    print("奖励一台笔记本")
else:
    if score >= 80:
        print("奖励一套Python学习教程")
    else:
        if score >= 70:
            print("奖励一支笔")
        else:
            print("重做试卷")
            
#elif
score = int(input("2.请输入您的成绩"))
if score >= 90:
    print("奖励一台笔记本")
elif score >= 80:
    print("奖励一套Python学习教程")
elif core >= 70:
    print("奖励一支笔")
else:
    print("重做试卷")






            
