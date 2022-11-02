import glob
from pathlib import Path

import Qt
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QTableWidget, QTableWidgetItem, QCheckBox, QLineEdit, QPushButton, QTableWidgetItem

# import manager.conf.conf_ui as conf_ui
from manager import conf, core, engine

from PySide2 import QtGui, QtCore

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # super is the keyword to ask for a parent
        QtCompat.loadUi(str(conf.ui_path), self)

        # Set window title
        self.setWindowTitle(conf.app_name)

        # Get running engine
        self.engine = engine.get()
        print(self.engine)

        # Create a list that will contain software to show
        self.software_names = []

        # Init check boxes
        self.software_checkboxes = []
        self.init_checkboxes(self)

        # Init dynamic buttons
        self.buttons = []
        self.init_dyn_buttons()

        self.connect()

    def connect(self):
        # Click somewhere on the table
        self.t_resume.clicked.connect(self.select_whole_row)
        # Click one of the dynamic checkboxes
        for i in range(len(self.software_checkboxes)):
            self.software_checkboxes[i].clicked.connect(self.do_soft_cb_click)

        # Click one of the dynamic buttons
        for i, button in enumerate(self.buttons):
            self.buttons[i].clicked.connect(self.do_click_on_dyn_button)

        # Click on "Quit" button
        self.pb_quit.clicked.connect(self.do_quit)

    # v Buttons ======================================================
    def do_open(self):
        # Get current cell
        active_cell = self.t_resume.currentItem()

        # Check if a row is selected
        if active_cell is not None:
            # Get current row
            current_row = self.t_resume.currentRow()
            # Get the "Full Address" column
            path_column = self.t_resume.indexFromItem(self.t_resume.findItems("D:", QtCore.Qt.MatchContains)[0]).column()
            # Get the selected row linked address
            address = self.t_resume.item(current_row, path_column).text()
            print(address)
            # Open file
            self.engine.open_file_from_path(address)
        # If not, returns an error - a window would be better
        else:
            print('Please select an item before clicking the \"Open\" button')

    def do_reference(self):
        print("Clicked on \"Reference\" button")

    def do_import(self):
        print("Clicked on \"Import\" button")

    def do_build(self):
        print("Clicked on \"Build\" button")

    def do_quit(self):
        app.exit()

    def init_dyn_buttons(self):
        print("Init buttons")
        # Get placeholder lay-out
        buttons_layout = self.pl_button.parentWidget()

        # Get all possible buttons
        buttons_names = self.engine.implement
        print(buttons_names)

        # Get the first button name
        first_button_caption = buttons_names[0]
        # Remplace its caption
        self.pl_button.setText(first_button_caption)
        # Put the name to low case and add the prefix
        first_button_name = f"cb_{first_button_caption.lower()}"
        # Remplace its name
        self.pl_button.setObjectName(first_button_name)
        # Add it in the list
        self.buttons.append(self.pl_button)

        # Create other buttons
        for i in range(len(buttons_names)-1):
            new_button_name = f"cb_{buttons_names[i+1].lower()}"
            new_button = QtWidgets.QPushButton(new_button_name, self)
            new_button.setText(buttons_names[i+1])
            buttons_layout.layout().addWidget(new_button)
            self.buttons.append(new_button)

    def do_click_on_dyn_button(self):
        print("Clicked on dynamic button")

    # ^ Buttons ======================================================
    # v Checkboxes ===================================================
    def init_checkboxes(self, current_layout):
        # Get placeholder layout
        soft_programs_layout = self.pl_software.parentWidget()

        # Get all possible software
        software_names = list(conf.software_programs.keys())
        # Remplace its caption
        self.pl_software.setText("All")
        # Remplace its name
        self.pl_software.setObjectName("cb_all_none")
        # Add it in the list
        self.software_checkboxes.append(self.pl_software)

        # Create other buttons
        for i in range(len(software_names)):
            new_box = QtWidgets.QCheckBox(software_names[i], self)
            soft_programs_layout.layout().addWidget(new_box)
            self.software_checkboxes.append(new_box)

    def rm_software_names_elem(self, software_name):
        if len(self.software_names) > 0:
            elem_to_rm_index = self.software_names.index(str(software_name))
            self.software_names.pop(elem_to_rm_index)
        # Shouldn't happen, but we'll print it just in case
        else:
            print('Can\'t remove an element from an empty list')

    def do_soft_cb_click(self):
        check_box = self.sender()
        check_box_text = check_box.text()
        check_box_status = check_box.isChecked()

        if check_box.objectName() == "cb_all_none":
            # If the "All" check box is checked
            if check_box_status and check_box_text == "All":
                # Empty software_names list
                self.software_names.clear()
                # Check all check boxes
                for check_box in self.software_checkboxes:
                    check_box.setChecked(True)
                # Fill the software_names all software names from the config file
                for key in conf.software_programs.keys():
                    self.software_names.append(str(key))
                # Change its text to "None"
                self.sender().setText("None")
                # Uncheck it
                self.sender().setChecked(False)
            # If the "None" check box is checked
            elif check_box_text == "None":
                # Empty software_names list
                self.software_names.clear()
                # Uncheck all check boxes
                for check_box in self.software_checkboxes:
                    check_box.setChecked(False)
                # Change its text to "All"
                self.sender().setText("All")
        # If another check box has been checked, add the software to the list
        elif check_box_status:
            self.software_names.append(check_box_text)
        # Otherwise, remove it
        else:
            self.rm_software_names_elem(str(check_box_text))

        # Update the data
        updt_data = list(core.get_entities("micromovie", self.software_names))
        # Update the table
        self.init_files_table(updt_data)

    # ^ Checkboxes ===================================================
    # v Tables =======================================================
    def select_whole_row(self):
        # Get current row
        current_row = self.t_resume.currentRow()
        # Select current row
        self.t_resume.selectRow(current_row)

    def fill_table(self, data_list):
        # Fill table
        for i in range(len(data_list)):
            # Get the current dictionary
            dict_from_list = data_list[i][0]
            # Get type
            item_type = dict_from_list["type"]

            if item_type == 'assets':
                # Init the elements
                qt_tab_item_type = QTableWidgetItem(dict_from_list["type"])
                qt_tab_item_category = QTableWidgetItem(dict_from_list["category"])
                qt_tab_item_name = QTableWidgetItem(dict_from_list["name"])
                qt_tab_item_task = QTableWidgetItem(dict_from_list["task"])
                qt_tab_item_version_nb = QTableWidgetItem(dict_from_list["versionNb"])
                qt_tab_item_state = QTableWidgetItem(dict_from_list["state"])

                file_name = f'{dict_from_list["name"]}_{dict_from_list["state"]}.{dict_from_list["ext"]}'
                qt_tab_item_file_name = QTableWidgetItem(file_name)

                qt_tab_item_software = QTableWidgetItem(data_list[i][1])
                qt_tab_item_address = QTableWidgetItem(core.format(dict_from_list))

                # Fill the table with the elements
                self.t_resume.setItem(i, 0, qt_tab_item_type)
                self.t_resume.setItem(i, 1, qt_tab_item_category)
                self.t_resume.setItem(i, 2, qt_tab_item_name)
                self.t_resume.setItem(i, 3, qt_tab_item_task)
                self.t_resume.setItem(i, 4, qt_tab_item_version_nb)
                self.t_resume.setItem(i, 5, qt_tab_item_state)
                self.t_resume.setItem(i, 6, qt_tab_item_file_name)

                '''
                self.t_resume.setItem(i, 1, qt_tab_item_software)
                self.t_resume.setItem(i, 2, qt_tab_item_address)
                '''

            if item_type == 'shots':
                # Init the elements
                qt_tab_item_type = QTableWidgetItem(dict_from_list["type"])
                qt_tab_item_sq_nb = QTableWidgetItem(f'sq{dict_from_list["sqNb"]}')
                qt_tab_item_sh_nb = QTableWidgetItem(f'sh{dict_from_list["shNb"]}')
                qt_tab_item_task = QTableWidgetItem(dict_from_list["task"])
                qt_tab_item_version_nb = QTableWidgetItem(f'v{dict_from_list["versionNb"]}')
                qt_tab_item_state = QTableWidgetItem(dict_from_list["state"])

                file_name = f'sh{dict_from_list["shNb"]}_{dict_from_list["state"]}.{dict_from_list["ext"]}'
                qt_tab_item_file_name = QTableWidgetItem(file_name)

                # Fill the table with the elements
                self.t_resume.setItem(i, 0, qt_tab_item_type)
                self.t_resume.setItem(i, 1, qt_tab_item_sq_nb)
                self.t_resume.setItem(i, 2, qt_tab_item_sh_nb)
                self.t_resume.setItem(i, 3, qt_tab_item_task)
                self.t_resume.setItem(i, 4, qt_tab_item_version_nb)
                self.t_resume.setItem(i, 5, qt_tab_item_state)
                self.t_resume.setItem(i, 6, qt_tab_item_file_name)

    def init_files_table(self, data_list):
        # Turn the table to a non-editable one
        self.t_resume.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Add new rows
        self.t_resume.setRowCount(len(data_list))

        # TEMP =================================
        # Add new columns
        self.t_resume.setColumnCount(len(data_list[2][0].keys()))  # <-- temp

        # Prepare columns names
        labels = ["Type", "Category", "Name", "Task", "Vers. nb", "State", "File name"]
        # Rename columns
        self.t_resume.setHorizontalHeaderLabels(labels)
        # ======================================

        # Fill rows
        self.fill_table(data_list)
        # Resize table automatically
        self.t_resume.resizeColumnsToContents()

    # ^ Tables =======================================================

# v =============================================================╗
# v Launch                                                       ║
def open_window():
    w = Window()
    w.show()

    # Harcoded init test
    w.software_names.append("Maya")
    w.software_checkboxes[1].setChecked(True)

    data_list = list(core.get_entities("micromovie", w.software_names))
    w.init_files_table(data_list)

# v Launch                                                       ║
# ^ =============================================================╝
# v =============================================================╗
# v Main                                                         ║

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    open_window()

    app.exec_()
# ^ Main                                                         ║
# ^ =============================================================╝