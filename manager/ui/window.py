from pathlib import Path

import Qt
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem

ui_path = Path(__file__).parent / "qt" / "window.ui"

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # super is the keyword to ask for a parent
        print("init done")
        QtCompat.loadUi(str(ui_path), self)
        self.connect()
        self.le_demo.setText("Bip")
        self.setWindowTitle("Pipeline22")

    def connect(self):
        self.pb_open.clicked.connect(self.do_open)

    # v Buttons click ================================================
    def do_open(self):
        print("Clicked on \"Open\" button")
        print(f"Line edit: {self.le_demo.text()}")

    def do_build(self):
        print("Clicked on \"Build\" button")

    # ^ ==============================================================
    # v Tables =======================================================
    def init_files_table(self, fileList):
        self.t_resume.setRowCount(len(fileList))

        for i in range(len(fileList)):
            qt_table_widget_item = QTableWidgetItem(fileList[i])
            self.t_resume.setItem(i, 0, qt_table_widget_item)

    # ^ Tables =======================================================

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    w = Window()
    w.show()

    dataList = ["MayaFile1", "MayaFile2", "MayaFile3", "MayaFile4"]
    w.init_files_table(dataList)

    app.exec_()
