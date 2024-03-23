from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
from cron import CronExpression
from generate_cron import GenerateCron

class CronRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.parseUI = CronExpression()
        self.generateUI = GenerateCron()

    def initUI(self):
        self.setWindowTitle('Cron 运行器')
        self.setWindowIcon(QIcon('img/tools.png'))
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        parseBtn = QPushButton('解析 Cron 表达式')
        parseBtn.clicked.connect(self.parseCron)
        layout.addWidget(parseBtn)

        generateBtn = QPushButton('生成 Cron 表达式')
        generateBtn.clicked.connect(self.generateCron)
        layout.addWidget(generateBtn)

        self.setLayout(layout)



    def parseCron(self):
        self.generateUI.hide()
        self.parseUI.show()

    def generateCron(self):
        self.parseUI.hide()
        self.generateUI.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CronRunner()
    demo.show()
    sys.exit(app.exec())


