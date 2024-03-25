from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *

'''
1.sqlite 安装教程 : https://doc.yonyoucloud.com/doc/wiki/project/sqlite/sqlite-installation.html
最新的版的压缩包，解压之后可以直接使用，不需要make过程，解压之后就有sqlite3可执行文件了

2.创建一个db后缀的文件，替换掉我的那个文件地址即可跑起来
'''
class SqlQuery():
    def __init__(self):
        pass

    def connect_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('/Users/zhaojun/develop/sqlit/dbquery.db')
        isOpen = db.open()
        if(isOpen):
            print("数据库连接成功")
            self.db = db
            self.writeModel = QSqlQuery(db=self.db)
            self.queryModel = QSqlQueryModel()
        else:
            print("数据库连接失败")
        return db
    
    def query(self, sql):
        self.queryModel.setQuery(sql)
    
    def write(self, sql):
        self.writeModel.exec(sql)
    
    def get_tables(self):
        return self.db.tables()

    def close_db(self):
        self.db.close()


if __name__ == "__main__":
    sqlQuery = SqlQuery()
    db = sqlQuery.connect_db()
    queryModel = QSqlQuery()
    queryModel.exec("create table people(id int primary key, name varchar(20), age int)")
    queryModel.exec("insert into people(id, name, age) values(1, 'zhaojun', 20)")
    queryModel.exec("insert into people(id, name, age) values(2, 'zhaojun2', 20)")
    queryModel.exec("insert into people(id, name, age) values(3, 'zhaojun3', 20)")
    queryModel.exec("select * from people")
    while queryModel.next():
        print(queryModel.value(0), queryModel.value(1), queryModel.value(2))
    
    sqlQuery.close_db()
    
