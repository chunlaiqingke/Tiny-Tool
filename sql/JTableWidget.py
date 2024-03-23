## QTableWidget
'''
包含分页插件
'''

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

class JTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def prepare_data(self, data):
        self.data = data
    
    def initUI(self):
        self.tableWidget = QTableWidget()
        self.pre_page = QPushButton("上一页")
        self.pre_page.clicked.connect(self.prepage)
        self.next_page = QPushButton("下一页")
        self.next_page.clicked.connect(self.nextpage)

        self.page_size_label = QLabel("每页")
        self.page_size = QComboBox()
        self.page_size.addItem("10")
        self.page_size.addItem("20")
        self.page_size.addItem("50")
        self.page_size.addItem("100")
        self.page_size.setCurrentIndex(0)
        self.page_size.currentIndexChanged.connect(self.setPageSize)
        self.page_count = 0
        self.page_label = QLabel(f"条, 共{self.page_count}页")

    def setData(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

    def prepage():
        pass

    def nextpage():
        pass

    def setPageSize():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = JTableWidget()
    ex.show()
    sys.exit(app.exec())