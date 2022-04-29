import sqlite3 # 导入sqlite3模块

conn = sqlite3.connect("text.bd") # 创建数据库
cursor = conn.cursor() # 创建游标对象

cursor.execute('''create table if not exists goods(
id int,
name text,
num int,
price int,
weight int,
place text)''') # 创建表对象

# 插入单行
cursor.execute("insert into goods(id,name,num,price,weight,place) values(2344,'toothbrush',1234,12,23,'Guangdong')")

# 插入多行
cursor.execute('''
insert into goods(id,name,num,price,weight,place) 
select 2344,'toothbrush',1234,12,23,'Guangdong' 
union select 34,'tea',34454,234,45,'Luzhou'
''')


# 删除
# delete删除满足条件的行
# delete from 表名 where 删除条件
cursor.execute('''
delete from goods where name = "toothbrush"
''')

# delete清空表数据 (框架依旧存在)
# delete from 表名
cursor.execute("delete from goods")

# delete删除整个表
cursor.execute("drop table goods")

conn.commit()
conn.close()