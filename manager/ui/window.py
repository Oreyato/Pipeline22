import glob
from pathlib import Path

import Qt
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QTableWidget, QTableWidgetItem, \
    QCheckBox, QLineEdit, QPushButton, QTableWidgetItem

# import manager.conf.conf_ui as conf_ui
from manager import conf, core, engine

from PySide2 import QtGui, QtCore


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  # super is the keyword to ask for a parent
        QtCompat.loadUi(str(conf.ui_path), self)

        # Set UserRole variable
        self.UserRole = QtCore.Qt.UserRole

        # Set window title
        self.setWindowTitle(conf.app_name)

        # Get running engine
        self.engine = engine.get()
        print(self.engine)

        # Create a list that will contain software to show
        self.software_names = []
        # Populate it with all possible software
        for software in conf.software_programs:
            self.software_names.append(software)

        # Init drop down menus
        self.software_dropdowns = []
        self.init_dropdowns()

        # Init check boxes
        self.software_checkboxes = []
        self.init_checkboxes(self)

        # Init dynamic buttons
        self.buttons = []
        self.init_dyn_buttons()

        self.connect()

    def connect(self):
        # Click on one of the dropdown menus for project and type
        self.projects_cb.currentIndexChanged.connect(self.are_dropdowns_set)
        self.types_cb.currentIndexChanged.connect(self.are_dropdowns_set)

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

    # v Dropdown menus ===============================================
    def init_dropdowns(self):
        # Projects ==============================
        # Clear the test variables
        self.projects_cb.clear()
        # Set a placeholder text
        # self.projects_cb.setPlaceholderText("<Project>")
        # Get all possible projects
        projects = list(conf.projects.keys())
        # Add it to the projects combo box
        self.projects_cb.addItems(projects)
        # Set index to the placeholder
        # self.projects_cb.setCurrentIndex(-1)

        # Types == ==============================
        # Clear the test variables
        self.types_cb.clear()
        # Get all possible types
        types = conf.types
        # Add it to the types combo box
        self.types_cb.addItems(types)

    def are_dropdowns_set(self):
        print(self.projects_cb.currentText())

        # Check if both the project and the type have been set
        if self.projects_cb.currentIndex() is not 0 and self.types_cb.currentIndex() is not 0:
            data_list = list(core.get_entities(self.projects_cb.currentText(), self.software_names))
            self.init_files_table(data_list)

    # ^ Dropdown menus ===============================================
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
            new_box.setChecked(True)
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
    # v Buttons ======================================================
    def do_open(self):
        # Get current cell
        active_cell = self.t_resume.currentItem()

        # Check if a row is selected
        if active_cell is not None:
            # Get current row
            current_row = self.t_resume.currentRow()
            # Get the "Full Address" column
            path_column = self.t_resume.indexFromItem(
                self.t_resume.findItems("D:", QtCore.Qt.MatchContains)[0]).column()
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
        for i in range(len(buttons_names) - 1):
            new_button_name = f"cb_{buttons_names[i + 1].lower()}"
            new_button = QtWidgets.QPushButton(new_button_name, self)
            new_button.setText(buttons_names[i + 1])
            buttons_layout.layout().addWidget(new_button)
            self.buttons.append(new_button)

    def do_click_on_dyn_button(self):
        print("Clicked on dynamic button")

    # ^ Buttons ======================================================
    # v Tables =======================================================
    def add_table_widget_item(self, parent, sid, label, row, column=1):
        item = QtWidgets.QTableWidgetItem()

        item.setData(self.UserRole, sid)
        item.setText(str(label))
        parent.setItem(row, column, item)

        return item

    def select_whole_row(self):
        # Get current row
        current_row = self.t_resume.currentRow()
        # Select current row
        self.t_resume.selectRow(current_row)

    def fill_table(self, data_list):
        # Fill table
        for i in range(len(data_list)):
            # Get the current dictionary
            entity = data_list[i][0]
            # Get type
            item_type = entity["type"]

            if item_type == 'assets':
                # Init the elements
                qt_tab_item_type = QTableWidgetItem(entity["type"])
                qt_tab_item_category = QTableWidgetItem(entity["category"])
                qt_tab_item_name = QTableWidgetItem(entity["name"])
                qt_tab_item_task = QTableWidgetItem(entity["task"])
                qt_tab_item_version_nb = QTableWidgetItem(f'v{entity["versionNb"]}')
                qt_tab_item_state = QTableWidgetItem(entity["state"])

                # Last item storing the full entity but showing a string
                file_name = f'{entity["name"]}_{entity["state"]}.{entity["ext"]}'
                last_item = QTableWidgetItem()
                last_item.setData(self.UserRole, entity)
                last_item.setText(file_name)
                # To access the data:
                # last_item.data(UserRole)

                qt_tab_item_software = QTableWidgetItem(data_list[i][1])
                qt_tab_item_address = QTableWidgetItem(core.format(entity))

                # Fill the table with the elements
                self.t_resume.setItem(i, 0, qt_tab_item_type)
                self.t_resume.setItem(i, 1, qt_tab_item_category)
                self.t_resume.setItem(i, 2, qt_tab_item_name)
                self.t_resume.setItem(i, 3, qt_tab_item_task)
                self.t_resume.setItem(i, 4, qt_tab_item_version_nb)
                self.t_resume.setItem(i, 5, qt_tab_item_state)
                self.t_resume.setItem(i, 6, last_item)

                '''
                self.t_resume.setItem(i, 1, qt_tab_item_software)
                self.t_resume.setItem(i, 2, qt_tab_item_address)
                '''

            if item_type == 'shots':
                # Init the elements
                qt_tab_item_type = QTableWidgetItem(entity["type"])
                qt_tab_item_sq_nb = QTableWidgetItem(f'sq{entity["sqNb"]}')
                qt_tab_item_sh_nb = QTableWidgetItem(f'sh{entity["shNb"]}')
                qt_tab_item_task = QTableWidgetItem(entity["task"])
                qt_tab_item_version_nb = QTableWidgetItem(f'v{entity["versionNb"]}')
                qt_tab_item_state = QTableWidgetItem(entity["state"])

                # Last item storing the full entity
                file_name = f'sh{entity["shNb"]}_{entity["state"]}.{entity["ext"]}'
                last_item = QTableWidgetItem()
                last_item.setData(self.UserRole, entity)
                last_item.setText(file_name)

                # Fill the table with the elements
                self.t_resume.setItem(i, 0, qt_tab_item_type)
                self.t_resume.setItem(i, 1, qt_tab_item_sq_nb)
                self.t_resume.setItem(i, 2, qt_tab_item_sh_nb)
                self.t_resume.setItem(i, 3, qt_tab_item_task)
                self.t_resume.setItem(i, 4, qt_tab_item_version_nb)
                self.t_resume.setItem(i, 5, qt_tab_item_state)
                self.t_resume.setItem(i, 6, last_item)

    def init_files_table(self, data_list):
        # Turn the table to a non-editable one
        self.t_resume.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Add new rows
        self.t_resume.setRowCount(len(data_list))

        # TEMP =================================
        # Add new columns
        self.t_resume.setColumnCount(len(data_list[0][0].keys()))  # <-- temp, raises an error
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
