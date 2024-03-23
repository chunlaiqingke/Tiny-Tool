from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import json
import time
import os
from parse_json_from_file import JsonUtil


class JSONParser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.showMaximized()
        # 创建一个水平布局
        hlayout = QHBoxLayout(self)

        inVlayout = QVBoxLayout()
        inHlayout = QHBoxLayout()
        jsonLabel = QLabel("jsonPath:")
        self.jsonPath = QComboBox()
        self.jsonPath.addItem("$.res.data[0]")
        self.jsonPath.setEditable(True)
        self.jsonPath.setCurrentText("")
        self.jsonPath.setPlaceholderText("请输入jsonPath")
        inHlayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        inHlayout.addWidget(jsonLabel)
        inHlayout.addWidget(self.jsonPath)
        inHlayout.setStretchFactor(jsonLabel, 1)
        inHlayout.setStretchFactor(self.jsonPath, 9)
        self.input = QTextEdit()
        self.input.setFocus()
        inVlayout.addLayout(inHlayout)
        inVlayout.addWidget(self.input)

        outVlayout = QVBoxLayout()
        outHlayout = QHBoxLayout()
        dirChoose = QPushButton("选择保存路径:")
        
        dirChoose.clicked.connect(self.chooseDir)
        outHlayout.addWidget(dirChoose)
        self.dirPath = QLabel()
        outHlayout.addWidget(self.dirPath)
        
        outHlayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.output = QTextEdit()
        outVlayout.addLayout(outHlayout)
        outVlayout.addWidget(self.output)

        midVlayout = QVBoxLayout(self)
        filterBtn = QPushButton("filter")
        filterBtn.setToolTip("提取jsonpath")
        filterBtn.clicked.connect(self.filt)
        midVlayout.addWidget(filterBtn)
        formatBtn = QPushButton("format")
        formatBtn.setToolTip("格式化json")
        formatBtn.clicked.connect(self.formatJSON)
        midVlayout.addWidget(formatBtn)
        self.saveBtn = QPushButton("save")
        self.saveBtn.setToolTip("按照上面的路径保存文件")
        self.saveBtn.clicked.connect(self.saveFile)
        midVlayout.addWidget(self.saveBtn)
        midVlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hlayout.addLayout(inVlayout)
        hlayout.addLayout(midVlayout)
        hlayout.addLayout(outVlayout)

        self.setLayout(hlayout)
        self.setWindowTitle('JSON格式化工具')
        self.setWindowIcon(QIcon('tools.png'))


    def chooseDir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择文件夹")
        self.dirPath.setText(dir)
    
    def formatJSON(self):
        inputText = self.input.toPlainText()
        if(inputText):
            try:
                jsonText = self._format(inputText)
                self.output.setText(jsonText)
            except:
                self.output.setText("json 格式有问题")

    def saveFile(self):
        dirPath = self.dirPath.text()
        if(not dirPath):
            QMessageBox.warning(self, "提示", "请先选择文件夹", QMessageBox.StandardButton.Yes)
            return
        filename = time.strftime("%Y%m%d%H%M%S", time.localtime())
        file_path = os.path.join(dirPath, filename)
        if(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.output.toPlainText())
    
    def loadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "JSON Files (*.json)")
        if(fileName):
            with open(fileName, "r", encoding="utf-8") as f:
                self.input.setText(f.read())
        

    def filt(self):
        json = self.input.toPlainText()
        path = self.jsonPath.currentText()
        format_json = JsonUtil.jsonPathStr(json, path)
        self.output.setText(format_json)

    def _format(self, inputText):
        return json.dumps(json.loads(inputText), indent=4, ensure_ascii=False)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = JSONParser()
    demo.show()
    sys.exit(app.exec())


