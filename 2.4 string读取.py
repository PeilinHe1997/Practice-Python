# Python的基本数据类型

#       一、字符串类型string/str
# 可用单引号，双引号，三引号
name1 = '小张'
name2 = "小张"
name3 = '''
我是小明
'''
name4 = """
我是小明
"""
print(name1)
print(name2)
print(name3)
print(name4)

#       二、读取、合并、修改、删除
#字符串的读取操作
name = "abcdefghi,jk"
print("name = ",name)
print("name[:4] is ",name[:4])#不包括4，只包括0123
print("name[2:4] is ",name[2:4])#不包括4，包括23
print("name[9:12] is ",name[9:12])
print("name[:] is ",name[:])
