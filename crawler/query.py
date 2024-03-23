from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import sys
import os



class Query(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 1000, 800)
        self.setWindowTitle('Query')

        layout = QHBoxLayout()

        self.cookie_label = QLabel("Cookie:")
        self.cookie_input = QTextEdit()
        self.sql_label = QLabel("Sql:")
        self.sql_input = QTextEdit()
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.cookie_label)
        left_layout.addWidget(self.cookie_input, stretch=1)
        left_layout.addWidget(self.sql_label)
        left_layout.addWidget(self.sql_input, stretch=2)
        layout.addLayout(left_layout)

        self.execute_button = QPushButton("执行")
        self.auto_execute_button = QPushButton("全自动")
        mid_layout = QVBoxLayout()
        mid_layout.addWidget(self.execute_button)
        mid_layout.addWidget(self.auto_execute_button)
        mid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(mid_layout)

        self.dirChoose = QPushButton("选择空文件夹:")
        self.dirChoose.clicked.connect(self.chooseDir)
        self.dir_label = QLabel()
        right_buttom_layout = QHBoxLayout()
        right_buttom_layout.addWidget(self.dirChoose)
        right_buttom_layout.addWidget(self.dir_label)
        right_buttom_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.result_label = QLabel("结果:")
        self.result_output = QTextEdit()
        right_layout = QVBoxLayout()

        self.file_list = QListWidget()
        for i in range(10):
            self.file_list.insertItem(0, f"File {i+1}")
        right_layout.addWidget(self.result_label)
        right_layout.addWidget(self.result_output, stretch=2)
        right_layout.addLayout(right_buttom_layout)
        right_layout.addWidget(self.file_list, stretch=1)

        layout.addLayout(right_layout)
        self.setLayout(layout)


    def chooseDir(self):
        # 选择保存路径
        dir_path = QFileDialog.getExistingDirectory(self, "选择保存路径")
        self.dir_label.setText(dir_path)

    def loadRemoteData(self):
        # 加载远程数据
        pass

    def saveLocalData(self, file_name, data):
        # 保存本地数据
        path = self.dir_label.text()
        file = os.path.join(path, file_name)
        with open(file, 'w') as f:
            f.write(data)

    def executeQuery(self):
        # 执行查询
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Query()
    demo.show()
    sys.exit(app.exec())


