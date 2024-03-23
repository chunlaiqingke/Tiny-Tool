from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import sys
import os

import pathlib
path_top = pathlib.Path(__file__).parent.parent
if str(path_top) not in sys.path:
    sys.path.append(str(path_top))

import cron


class DBQuery(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cookie = ""
        

    def initUI(self):

        self.setWindowTitle('DBQuery')
        self.setGeometry(200, 200, 800, 600)

        layout = QHBoxLayout()

        leftlayout = QVBoxLayout()
        self.cookie_btn = QPushButton("Cookie")
        self.cookie_btn.clicked.connect(self.cookieClicked)
        leftlayout.addWidget(self.cookie_btn)
        server_label = QLabel("库:")
        self.dbserver = QComboBox()
        server_layout = QHBoxLayout()
        server_layout.addWidget(server_label, stretch=1)
        server_layout.addWidget(self.dbserver, stretch=6)
        server_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        sql_label = QLabel("数据库表:")
        self.table_list = QListWidget()
        self.table_list.addItems(["表1", "表2", "表3"])
        leftlayout.addLayout(server_layout)
        leftlayout.addWidget(sql_label)
        leftlayout.addWidget(self.table_list)
        layout.addLayout(leftlayout, stretch=1)

        
        rightTopLayout = QVBoxLayout()
        rightTopLayout.addWidget(QLabel("输入sql:"))
        self.sql = QTextEdit()
        rightTopLayout.addWidget(self.sql, stretch=2)
        self.queryLayout = QHBoxLayout()
        self.query_button = QPushButton("查询")
        self.query_button.clicked.connect(self.queryClicked)
        self.queryLayout.addWidget(self.query_button)
        self.export = QPushButton("导出")
        self.export.clicked.connect(self.exportClicked)
        self.queryLayout.addWidget(self.export)

        self.dirChoose = QPushButton("选择")
        self.dirChoose.clicked.connect(self.chooseDir)
        self.dir_label = QLabel("未选择导出文件夹")
        self.queryLayout.addWidget(self.dirChoose)
        self.queryLayout.addWidget(self.dir_label)
        self.queryLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_table = QTableWidget()
        rightTopLayout.addLayout(self.queryLayout)
        rightTopLayout.addWidget(self.result_table, stretch=4)

        layout.addLayout(rightTopLayout, stretch=3)
        
        self.setLayout(layout)

    
    def cookieClicked(self):
        c, ok = QInputDialog.getMultiLineText(self, "输入cookie", "输入cookie", self.cookie)
        if ok:
            self.cookie = c

    def queryClicked(self):
        data = [[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]
        self.result_table.clear()
        self.result_table.setColumnCount(len(data[0]))
        self.result_table.setRowCount(len(data))
        self.result_table.setHorizontalHeaderLabels(["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10"])
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.result_table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def exportClicked(self):
        pass

    def chooseDir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择空文件夹")
        if dir:
            self.dir_label.setText(dir)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DBQuery()
    window.show()
    sys.exit(app.exec())