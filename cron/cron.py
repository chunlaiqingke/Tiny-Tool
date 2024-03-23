# cron表达式解析
# 这个croniter用起来感觉好多bug，不知道为啥 文档地址：https://github.com/kiorky/croniter
# 可能是我不会用，还是规则和正常的cron不一样，谁知道的可以评论一下

from PyQt6.QtWidgets import *
import sys
from croniter import croniter, CroniterBadCronError, CroniterNotAlphaError
from datetime import datetime

class CronExpression(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cron Expression Parser')
        self.setGeometry(300, 300, 500, 400)

        head = QGridLayout()
        self.input_label = QLabel('Cron 表达式:', self)
        self.input = QLineEdit()
        self.time_label = QLabel('时间:', self)
        self.time_input = QLineEdit()
        head.addWidget(self.input_label, 0, 0)
        head.addWidget(self.input, 0, 1)
        head.addWidget(self.time_label, 1, 0)
        head.addWidget(self.time_input, 1, 1)


        ops = QHBoxLayout()
        self.match_button = QPushButton('匹配', self)
        self.match_button.clicked.connect(self.matchCron)
        self.parse_button = QPushButton('查看最近即将执行的几条时间', self)
        self.parse_button.clicked.connect(self.parseCron)
        ops.addWidget(self.match_button)
        ops.addWidget(self.parse_button)
        self.output= QTextEdit()
        
        body = QVBoxLayout()
        body.addLayout(head)
        body.addLayout(ops)
        body.addWidget(self.output)

        self.setLayout(body)


    def parseCron(self):
        input_text = self.input.text()
        self.output.clear()
        
        try:
            cron = croniter(input_text, datetime.now())
            for i in range(5):
                next_time = cron.get_next(datetime)
                self.output.append(f"下一次执行时间: {next_time} \n")
        except CroniterNotAlphaError as e:
            self.output.setText("不兼容的表达式")
        except CroniterBadCronError as e:
            self.output.setText("表达式有问题")


    def matchCron(self):
        input_text = self.input.text()
        time_str = self.time_input.text()
        self.output.clear()
        try:
            time = datetime.strptime(time_str.strip(), '%Y-%m-%d %H:%M:%S')
            is_match = croniter.match(input_text, time)
            self.output.setText(f"时间 {time_str} 是否匹配: {is_match}")
        except ValueError as e:
            self.output.setText("时间格式错误")
        

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CronExpression()
    demo.show()
    sys.exit(app.exec())


        