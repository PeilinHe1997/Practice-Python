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

# 三个双引号表示多行注释，也表示跨多行的字符串。这里的SQL语句就写在多行字符串中。
# 如果goods表创建了就会覆盖，如果没有创建就创建一个表。
# id int primary key auto increment not null
# 字段名 类型 约束：主键自增长，且不能为空，不能重复。

# cursor.execute(写SQL语法) # 增删改查

conn.commit() # 保存数据
conn.close() # 关闭数据库
