## QTableWidget
'''
包含分页插件
'''

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import time

class JTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initConnect()
        self.thread = ExportThread()
        self.thread.signal[int].connect(self.export)

    def prepare_data(self, data):
        self.data = data
    
    def initUI(self):
        self.tableWidget = QTableWidget()
        self.export_btn = QPushButton("导出")
        self.pre_page = QPushButton("上一页")
        self.next_page = QPushButton("下一页")

        self.page_size_label = QLabel("每页")
        self.page_size = QComboBox()
        self.page_size.addItem("10")
        self.page_size.addItem("20")
        self.page_size.addItem("50")
        self.page_size.addItem("100")
        self.page_size.setCurrentIndex(0)
        self.page_count = 0
        self.page_label = QLabel(f"条, 共{self.page_count}页")
        
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        
        pageLayout = QHBoxLayout()
        pageLayout.addWidget(self.export_btn)
        pageLayout.addWidget(self.pre_page)
        pageLayout.addWidget(self.next_page)
        pageLayout.addWidget(self.page_size_label)
        pageLayout.addWidget(self.page_size)
        pageLayout.addWidget(self.page_label)
        layout.addLayout(pageLayout)
        self.setLayout(layout)
        
    def initConnect(self):
        self.export_btn.clicked.connect(self.export_click)
        self.pre_page.clicked.connect(self.prepage)
        self.next_page.clicked.connect(self.nextpage)
        self.page_size.currentIndexChanged.connect(self.setPageSize)
        

    def setData(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

    def export_click(self):
        self.process = QProgressDialog()
        self.process.setWindowTitle("导出进度")
        self.process.canceled.connect(self.thread.stop)
        self.process.show()
        self.thread.start()
    
    def export(self, i):
        self.process.setValue(i)
        self.process.setLabelText(f"正在导出，请稍候...{self.process.value()}%")

    def prepage(self):
        pass

    def nextpage(self):
        pass

    def setPageSize(self):
        pass

        

class ExportThread(QThread):
    signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.interrupt = False

    def run(self):
        # 执行导出操作
        # 这里应该使用异步的方式进行导出，以避免阻塞主进程
        # 导出完成后，发送信号通知主进程更新界面
        for i in range(10):
            if not self.interrupt:
                time.sleep(1)
                self.signal.emit(i * 10 + 10)
            
    def stop(self):
        self.interrupt = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = JTableWidget()
    ex.show()
    sys.exit(app.exec())