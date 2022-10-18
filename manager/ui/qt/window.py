import Qt
from Qt.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # super is the keyword to ask for a parent

if __name__ == '__main__':
    w = Window()