# import json
import pymysql


class MysqlDatabases:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    charset='utf8',
                                    db='storehouse')

    def check_login(self, username, password):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = 'select username,password from user '

        cursor.execute(sql)
        users = cursor.fetchall()
        cursor.close()
        self.conn.close()


        for user in users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登录成功'

                else:
                    return False, '密码错误，请重新输入'

        return False, '登录失败，帐户名错误'




db = MysqlDatabases()
if __name__ == '__main__':
    db.check_login('username', 'password')

