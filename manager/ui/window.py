import glob
from pathlib import Path

import Qt
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem

# import manager.conf.conf_ui as conf_ui
from manager import conf
from manager import core

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # super is the keyword to ask for a parent
        print("init done")
        QtCompat.loadUi(str(conf.ui_path), self)
        self.connect()
        self.le_demo.setText("Bip")
        self.setWindowTitle(conf.app_name)

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
    def fill_table(self, file_list):
        # Fill table
        for i in range(len(file_list)):
            qt_tab_item_name = QTableWidgetItem(file_list[i][0])
            qt_tab_item_type = QTableWidgetItem(file_list[i][1])
            qt_tab_item_address = QTableWidgetItem(file_list[i][2])

            self.t_resume.setItem(i, 0, qt_tab_item_name)
            self.t_resume.setItem(i, 1, qt_tab_item_type)
            self.t_resume.setItem(i, 2, qt_tab_item_address)


    def get_whitelisted_files(self):
        # Look at checkboxes values
        print(conf.software_programs.keys())
        #                     v conf.software_programs.get('Maya')
        software_whitelist = ['Maya']
        file_list = []

        # Show files if their software is in the whitelist
        for data in data_list:
            for software in software_whitelist:
                if data[0][1] == software:
                    file_list = file_list + data

        return file_list


    def init_files_table(self, data_list):
        # Turn the table to a non-editable one
        self.t_resume.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Only get the files from whitelisted software
        file_list = self.get_whitelisted_files()

        # Add new rows
        self.t_resume.setRowCount(len(file_list))
        # Fill rows
        self.fill_table(file_list)
        # Resize table automatically
        self.t_resume.resizeColumnsToContents()

    # ^ Tables =======================================================

# v =============================================================╗
# v Create data list                                             ║

# From pipeline_path, get all Maya and Houdini files and store them in a list
# along with their type (Maya or Houdini file) and path (from pipeline_path)


def init_data_list():
    ma_datas = init_data_from_ext_and_soft("*.ma", "Maya")
    mb_datas = init_data_from_ext_and_soft("*.mb", "Maya")
    hipnc_datas = init_data_from_ext_and_soft("*.hipnc", "Houdini")

    data_list = [ma_datas, mb_datas, hipnc_datas]

    return data_list


def init_data_from_ext_and_soft(extension, software):
    # Get paths from extension
    paths_list = get_path_from_extension(extension)
    data_list = []

    # Get according names and set right software name
    for path in paths_list:
        file_name = get_file_name_from_path(path)
        data_list.append([file_name, software, path])

    return data_list


def get_path_from_extension(extension):
    paths_list = []

    project_path = Path(conf.pipeline_path) / conf.projects.get('micromovie')

    for item in project_path.rglob(extension):
        paths_list.append(str(item))

    return paths_list


def get_file_name_from_path(f_path):
    # find the correct path ==============================
    # remove the extension ===============
    # split the path
    split_path = f_path.split("\\")
    # get the last element of the list
    file_name = split_path[len(split_path) - 1]

    return file_name


# ^ Create data list                                             ║
# ^ =============================================================╝
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