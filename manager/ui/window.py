from pathlib import Path

import Qt
from Qt.QtWidgets import QMainWindow
from Qt import QtWidgets, QtCompat

ui_path = Path(__file__).parent / "qt" / "window.ui"

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # super is the keyword to ask for a parent
        print("init done")
        QtCompat.loadUi(str(ui_path), self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    w = Window()
    print(w)
    w.show()
    app.exec_()

