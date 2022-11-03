import Qt as Qt
import Qt.QtCore as QtCore

from Qt.QtWidgets import QLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, QListWidget

from Qt import QtWidgets, QtCompat
from manager.ui.window import Window


class EntityPartList(QtWidgets.QWidget):

    def __init__(self, label_p, entity_p, window_p):
        super(EntityPartList, self).__init__()
        self.label = label_p
        self.entity = entity_p
        self.window = window_p

    def init_list(self):
        # Prepare base name
        base_name = f'{self.label}_ent_part'

        # Prepare layout name
        layout_name = f'{base_name}_layout'
        # Create layout
        layout = QVBoxLayout()
        # Modify layout name
        layout.setObjectName(layout_name)

        # v Create label =================================================
        # Prepare label widget name
        label_name = f'{base_name}_label'
        # Create label widget
        entity_part_label = QLabel(label_name, self.window)
        # Set its text
        entity_part_label.setText(self.label)
        # Set its alignment
        entity_part_label.setAlignment(QtCore.Qt.AlignCenter)
        # ^ ==============================================================

        # Prepare list widget name
        list_name = f'{base_name}_list'
        # Create list widget
        entity_part_list = QListWidget()
        # Resize it
        entity_part_list.resize(300, 120)
        # Add an element inside
        entity_part_list.addItem("Item 1")

        # Add the widgets inside the layouts
        layout.addWidget(entity_part_label)
        layout.addWidget(entity_part_list)

        return layout


# Create a "main" to test the class
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QMainWindow()

    ep = EntityPartList("category", "entity", window)
    layout = ep.init_list()

    ep.setLayout(layout)


    ep.show()

    app.exec_()

