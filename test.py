import pymysql

conn = pymysql.connect(host='localhost',
                   user='root',
                   password='',
                   charset='utf8',
                   db='storehouse')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select username,password from user  '

cursor.execute(sql)
row = cursor.fetchall()
cursor.close()
conn.close()
print(row)