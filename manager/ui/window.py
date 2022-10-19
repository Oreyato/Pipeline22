import glob
from pathlib import Path

import Qt
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QTableWidget, QTableWidgetItem, QCheckBox

# import manager.conf.conf_ui as conf_ui
from manager import conf
from manager import core

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # super is the keyword to ask for a parent
        QtCompat.loadUi(str(conf.ui_path), self)

        self.le_demo.setText("Bip")
        self.setWindowTitle(conf.app_name)

        self.connect()

        current_layout = self
        self.init_checkboxes(self)

    def connect(self):
        self.pb_open.clicked.connect(self.do_open)
        self.pb_build.clicked.connect(self.do_build)

    # v Buttons click ================================================
    def do_open(self):
        print("Clicked on \"Open\" button")
        print(f"Line edit: {self.le_demo.text()}")

    def do_build(self):
        print("Clicked on \"Build\" button")

    # ^ ==============================================================
    # v Checkboxes ===================================================
    def init_checkboxes(self, current_layout):
        # Get placeholder lay-out
        soft_programs_layout = self.pl_software.parentWidget()

        # Get all possible software
        software_names = list(conf.software_programs.keys())
        # Remplace it's caption
        self.pl_software.setText("All")

        # Create other buttons
        for i in range(len(software_names)):
            new_box = QtWidgets.QCheckBox(software_names[i], self)
            soft_programs_layout.layout().addWidget(new_box)


    # ^ Checkboxes ===================================================
    # v Tables =======================================================
    def fill_table(self, data_list):
        # Fill table
        for i in range(len(data_list)):
            qt_tab_item_name = QTableWidgetItem(data_list[i][0])
            qt_tab_item_type = QTableWidgetItem(data_list[i][1])
            qt_tab_item_address = QTableWidgetItem(str(data_list[i][2]))

            self.t_resume.setItem(i, 0, qt_tab_item_name)
            self.t_resume.setItem(i, 1, qt_tab_item_type)
            self.t_resume.setItem(i, 2, qt_tab_item_address)


    def init_files_table(self, data_list):
        # Turn the table to a non-editable one
        self.t_resume.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Add new rows
        self.t_resume.setRowCount(len(data_list))
        # Fill rows
        self.fill_table(data_list)
        # Resize table automatically
        self.t_resume.resizeColumnsToContents()

    # ^ Tables =======================================================

# v =============================================================╗
# v Main                                                         ║

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    w = Window()
    w.show()

    data_list = list(core.init_data_list("micromovie", ["Maya", "Houdini"]))
    w.init_files_table(data_list)

    app.exec_()

# ^ Main                                                         ║
# ^ =============================================================╝