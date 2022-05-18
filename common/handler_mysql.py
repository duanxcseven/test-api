
import pymysql
import pymssql





class Handler_mysql:

    def __init__(self, host, port, user, password, *args, **kwargs):
        self.con = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=password,
                                   charset="utf8",
                                   # 设置游标返回对象格式
                                   cursorclass=pymysql.cursors.DictCursor)

    def sql_fetchall(self, sql):
        """
        :param sql: sql语句
        :return: 查询到的所有数据
        """
        with self.con as cur:
            cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def sql_fetchone(self, sql):
        '''

        :param sql: sql语句
        :return: 查询到的第一条数据
        '''
        with self.con as cur:
            cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def sql_res(self, sql):
        '''

        :param sql: sql语句
        :return: 查询到的数据条数
        '''
        with self.con as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    # 关闭链接
    def __del__(self):
        self.con.close()


class Handler_sql_server:

    def __init__(self,host,port,user,password,database,as_dict):
        self.con=pymssql.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 database=database,
                                 as_dict=as_dict)

    def sql_server(self,sql):
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def __del__(self):
        self.con.close()







