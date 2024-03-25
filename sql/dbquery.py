from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import sys
import os

from SqlQuery import SqlQuery

import pathlib
path_top = pathlib.Path(__file__).parent.parent
if str(path_top) not in sys.path:
    sys.path.append(str(path_top))



class DBQuery(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initAction()
        

    def initUI(self):

        self.setWindowTitle('DBQuery')
        self.setGeometry(200, 200, 800, 600)

        layout = QHBoxLayout()

        leftlayout = QVBoxLayout()
        self.login_btn = QPushButton("登录")
        leftlayout.addWidget(self.login_btn)
        sql_label = QLabel("数据库表:")
        self.table_list = QListWidget()
        self.table_list.addItems(["表1", "表2", "表3"])
        leftlayout.addWidget(sql_label)
        leftlayout.addWidget(self.table_list)
        layout.addLayout(leftlayout, stretch=1)

        
        rightTopLayout = QVBoxLayout()
        rightTopLayout.addWidget(QLabel("输入sql:"))
        self.sql = QTextEdit()
        rightTopLayout.addWidget(self.sql, stretch=2)
        self.queryLayout = QHBoxLayout()
        self.query_button = QPushButton("查询")
        self.queryLayout.addWidget(self.query_button)
        self.write_button = QPushButton("写入")
        self.queryLayout.addWidget(self.write_button)

        self.queryLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_table = QTableView()
        rightTopLayout.addLayout(self.queryLayout)
        rightTopLayout.addWidget(self.result_table, stretch=4)

        layout.addLayout(rightTopLayout, stretch=3)
        self.setLayout(layout)

    def initAction(self):
        # 登录
        self.login_btn.clicked.connect(self.loginClicked)
        # 查询
        self.query_button.clicked.connect(self.queryClicked)
        # 写入
        self.write_button.clicked.connect(self.writeClicked)
        

    
    def loginClicked(self):
        self.dbquery = SqlQuery()
        self.dbquery.connect_db()
        self.table_list.clear()
        self.table_list.addItems(self.dbquery.get_tables())


    def queryClicked(self):
        sql = self.sql.toPlainText()
        if sql:
            if sql.startswith("select"):
                self.dbquery.query(sql)
                self.result_table.setModel(self.dbquery.queryModel)
                # self.result_table.show()
            else:
                QMessageBox.warning(self, "警告", "请输入select语句")
        else :
            QMessageBox.warning(self, "警告", "请输入sql")
        

    def writeClicked(self):
        sql = self.sql.toPlainText()
        if sql:
            if sql.startswith("select"):
                QMessageBox.warning(self, "警告", "select语句,请选择查询按钮")
            else:
                try:
                    self.dbquery.write(sql)
                    QMessageBox.information(self, "警告", "成功")
                except:
                    QMessageBox.warning(self, "警告", "写入失败")

        else :
            QMessageBox.warning(self, "警告", "请输入sql")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DBQuery()
    window.show()
    sys.exit(app.exec())