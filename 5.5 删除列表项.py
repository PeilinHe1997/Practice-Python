#删除列表项
'''
1、clear()清空
2、pop()删除指定下标的列表项
3、remove() 删除指定列表项
4、del删除指定索引范围的列表

'''
star = ["双子","双鱼","金牛","蛇夫"]
#star.clear()
#star.pop(3)
#star.remove("蛇夫")
del star[0:3]
print(star)
