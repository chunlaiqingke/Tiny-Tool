from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from datetime import datetime



class GenerateCron(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Generate Cron')
        self.setGeometry(100, 100, 500, 400)
        self.setCentralWidget(QTextEdit())
        self.setWindowIcon(QIcon('../../img/json.png'))

        
        menuBar = self.menuBar()
        #这个方法必须调，否则在mac上出不来
        menuBar.setNativeMenuBar(False)

        s = QAction('秒', self)
        s.triggered.connect(self.showSecond)
        m = QAction('分钟', self)
        m.triggered.connect(self.showMinute)
        h = QAction('小时', self)
        h.triggered.connect(self.showHour)
        d = QAction('天', self)
        d.triggered.connect(self.showDay)
        mon = QAction('月', self)
        mon.triggered.connect(self.showMonth)
        menuBar.addAction(s)
        menuBar.addAction(m)
        menuBar.addAction(h)
        menuBar.addAction(d)
        menuBar.addAction(mon)

        self.parseLayout = QHBoxLayout()
        self.parseBtn = QPushButton('生成')
        self.parseBtn.clicked.connect(self.parse)
        self.parseRes = QLineEdit()
        self.parseLayout.addWidget(self.parseBtn)
        self.parseLayout.addWidget(self.parseRes)
        self.parseLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.second = Second()
        self.minute = Minute()
        self.hour = Hour()
        self.day = Day()
        self.month = Month()
        self.stackWidget = QStackedWidget()
        self.stackWidget.addWidget(self.second)
        self.stackWidget.addWidget(self.minute)
        self.stackWidget.addWidget(self.hour)
        self.stackWidget.addWidget(self.day)
        self.stackWidget.addWidget(self.month)


        self.center = QWidget()
        self.centerLayout = QVBoxLayout()
        self.centerLayout.addWidget(self.stackWidget)
        self.centerLayout.addLayout(self.parseLayout)
        self.center.setLayout(self.centerLayout)

        self.setCentralWidget(self.center)



    def showSecond(self):
        self.stackWidget.setCurrentIndex(0)
    
    def showMinute(self):
        self.stackWidget.setCurrentIndex(1)

    def showHour(self):
        self.stackWidget.setCurrentIndex(2)

    def showDay(self):
        self.stackWidget.setCurrentIndex(3)

    def showMonth(self):
        self.stackWidget.setCurrentIndex(4)

    def parse(self):
        self.parseRes.setText(self.getCronExpression())


    def getCronExpression(self):
        s = self.second.getCron()
        m = self.minute.getCron()
        h = self.hour.getCron()
        d = self.day.getCron()
        m = self.month.getCron()
        return f"{s} {m} {h} {d} {m}" 


'''
定义cron展示的抽象类
样式来自：https://cron.qqe2.com/
'''
class AbstractCronUI(QWidget):
    def __init__(self):
        super().__init__()
        self.key = self.getKey()
        self.initUI()

    def getKey(self):
        pass
    
    def initUI(self):
        self.customize_checkbox = []
        self.setWindowTitle('cron表达式生成器')

        self.setGeometry(100, 100, 500, 300)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        perLayout = QHBoxLayout()
        self.per = QRadioButton()
        self.per.setChecked(True)
        perLabel = QLabel(f'每{self.key} 允许的通配符[, - * /]')
        perLayout.addWidget(self.per)
        perLayout.addWidget(perLabel)
        perLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        periodLayout = QHBoxLayout()
        self.period = QRadioButton()
        periodLabel1 = QLabel('周期 从')
        self.periodInput1 = QLineEdit()
        periodLabel2 = QLabel('-')
        self.periodInput2 = QLineEdit()
        periodLabel3 = QLabel(f'{self.key}')
        periodLayout.addWidget(self.period)
        periodLayout.addWidget(periodLabel1)
        periodLayout.addWidget(self.periodInput1)
        periodLayout.addWidget(periodLabel2)
        periodLayout.addWidget(self.periodInput2)
        periodLayout.addWidget(periodLabel3)
        periodLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        spanLayout = QHBoxLayout()
        self.span = QRadioButton()
        spanLabel1 = QLabel('从')
        self.spanInput1 = QLineEdit()
        spanLabel2 = QLabel(f'{self.key}开始，每')
        self.spanInput2 = QLineEdit()
        spanLabel3 = QLabel(f'{self.key}执行一次')
        spanLayout.addWidget(self.span)
        spanLayout.addWidget(spanLabel1)
        spanLayout.addWidget(self.spanInput1)
        spanLayout.addWidget(spanLabel2)
        spanLayout.addWidget(self.spanInput2)
        spanLayout.addWidget(spanLabel3)
        spanLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        customizeLayout = QHBoxLayout()
        self.customizeBtn = QRadioButton()
        customizeLabel = QLabel('指定')
        customizeLayout.addWidget(self.customizeBtn)
        customizeLayout.addWidget(customizeLabel)
        customizeLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        girdlayout = self.customize()

        layout.addLayout(perLayout)
        layout.addLayout(periodLayout)
        layout.addLayout(spanLayout)
        layout.addLayout(customizeLayout)
        layout.addLayout(girdlayout)
        self.setLayout(layout)

    def customize(self):
        pass

    def getCron(self):
        if(self.per.isChecked()):
            return "*"
        elif(self.period.isChecked()):
            pi1 = self.periodInput1.text()
            pi2 = self.periodInput2.text()
            return pi1 + "-" + pi2
        elif(self.span.isChecked()):
            si1 = self.spanInput1.text()
            si2 = self.spanInput2.text()
            return si1 + "/" + si2
        elif(self.customizeBtn.isChecked()):
            cron = ""
            for i in range(self.customize_checkbox.length):
                if(self.customize_checkbox[i].isChecked()):
                    cron += str(i) + ","
            return cron[:-1]
        return ""
    

class Second(AbstractCronUI):
    def __init__(self):
        super().__init__()
        

    def getKey(self):
        return "秒"

    def customize(self):
        self.girdlayout = QGridLayout()
        for i in range(60):
            c0 = QCheckBox()
            l0 = QLabel(str(i))
            self.girdlayout.addWidget(c0,i//10,i%10 * 2)
            self.girdlayout.addWidget(l0,i//10,i%10 * 2 + 1)

            self.customize_checkbox.append(c0)
        return self.girdlayout
    


class Minute(AbstractCronUI):
    def __init__(self):
        super().__init__()
        
    def getKey(self):
        return "分钟"

    def customize(self):
        girdlayout = QGridLayout()
        for i in range(60):
            c0 = QCheckBox()
            l0 = QLabel(str(i))
            girdlayout.addWidget(c0,i//10,i%10 * 2)
            girdlayout.addWidget(l0,i//10,i%10 * 2 + 1)
            self.customize_checkbox.append(c0)
        return girdlayout


class Hour(AbstractCronUI):
    def __init__(self):
        super().__init__()
    
    def getKey(self):
        return "小时"
    
    def customize(self):
        girdlayout = QGridLayout()
        for i in range(24):
            c0 = QCheckBox()
            l0 = QLabel(str(i))
            girdlayout.addWidget(c0,i//12,i%12 * 2)
            girdlayout.addWidget(l0,i//12,i%12 * 2 + 1)
            self.customize_checkbox.append(c0)
        return girdlayout
    


class Day(AbstractCronUI):
    def __init__(self):
        super().__init__()

    def getKey(self):
        return "日"

    def customize(self):
        girdlayout = QGridLayout()
        for i in range(31):
            c0 = QCheckBox()
            l0 = QLabel(str(i + 1))
            girdlayout.addWidget(c0,i//7,i%7 * 2)
            girdlayout.addWidget(l0,i//7,i%7 * 2 + 1)
            self.customize_checkbox.append(c0)
        return girdlayout


class Month(AbstractCronUI):
    def __init__(self):
        super().__init__()

    def getKey(self):
        return "月"
    
    def customize(self):
        girdlayout = QGridLayout()
        for i in range(12):
            c0 = QCheckBox()
            l0 = QLabel(str(i + 1))
            girdlayout.addWidget(c0,i//12,i%12 * 2)
            girdlayout.addWidget(l0,i//12,i%12 * 2 + 1)
        return girdlayout



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = GenerateCron()
    demo.show()
    sys.exit(app.exec())
