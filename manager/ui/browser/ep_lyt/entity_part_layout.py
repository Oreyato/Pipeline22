import Qt as Qt
import Qt.QtCore as QtCore
from Qt.QtWidgets import QLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, QListWidget, QListWidgetItem
from Qt import QtWidgets, QtCompat

from manager import utils

class EntityPartLayout(QtWidgets.QWidget):
    def __init__(self, window_p, user_role_p, label_p, entities_p):
        """
        :param window_p: Window ref
        :param user_role_p: Qt UserRole
        :param label_p: entity label (str)
        :type label_p: str
        :param entities_p: entities ([entity]
        """
        # Call the parent constructor
        super(EntityPartLayout, self).__init__()
        # Attributes init ======================
        self.window = window_p
        self.user_role = user_role_p
        self.label = label_p
        self.entities = entities_p

        self.layout = None
        self.list_widget = None

        # Initialize
        self.init_layout()

        # Launch loops
        self.connect()

    # v =============================================================╗
    # v Methods                                                      ║
    # v Initialisations =================
    def init_layout(self):
        # Prepare base name
        base_name = f'{self.label}_ent_part'

        # v Create layout ================================================
        layout_name = f'{base_name}_layout'
        layout = QVBoxLayout()
        layout.setObjectName(layout_name)
        # ^ Create layout ================================================
        # v Create label =================================================
        label_name = f'{base_name}_label'
        entity_part_label = QLabel(self.window)
        entity_part_label.setObjectName(label_name)
        entity_part_label.setText(self.label)
        entity_part_label.setAlignment(QtCore.Qt.AlignCenter)
        # ^ Create label =================================================

        # Create list widget
        self.list_widget = self.create_list_widget(base_name)

        # Add the widgets inside the layouts
        layout.addWidget(entity_part_label)
        layout.addWidget(self.list_widget)

        self.layout = layout
        self.setLayout(layout)

    def create_list_widget(self, base_name_p):
        list_name = f'{base_name_p}_list'
        entity_part_list = QListWidget()
        entity_part_list.setObjectName(list_name)
        entity_part_list.setAlternatingRowColors(True)

        # Remove entities duplicates ===========
        # Prepare the lists
        unique_values = []
        unique_entities = []

        # Browse the entities list
        for entity in self.entities:
            # Keep track of the existence or not of a value
            exist = False

            dict_value = entity[self.label]

            # Browse the list that stores all known values
            for unique_value in unique_values:
                if dict_value == unique_value:
                    exist = True
            # If the value is not one of the already known values
            if not exist:
                unique_values.append(dict_value)
                unique_entities.append(entity)

        # Populate the list ====================
        for entity in unique_entities:
            list_item = QListWidgetItem()
            list_item.setData(self.user_role, entity)
            list_item.setText(entity[self.label])
            entity_part_list.addItem(list_item)

        return entity_part_list

    # v Getters / Setters ===============
    def get_layout(self):
        return self.layout

    # v Selected item ===================
    def selected_item(self):
        if len(self.list_widget.selectedItems()) is not 0:
            print(f'Selected \"{self.list_widget.selectedItems()[0].data(self.user_role)}\"')

        return self.list_widget.selectedItems()

    def connect(self):
        self.list_widget.itemClicked.connect(self.selected_item)

    # v Management ======================
    def empty_list(self):
        pass

    def close(self):
        pass

    # v Methods                                                      ║
    # ^ =============================================================╝
# v =============================================================╗
# v Main - test                                                  ║

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QMainWindow()

    entities = [{"KeyA": "ValueA1",
                 "KeyB": "ValueB1",
                 "KeyC": "ValueC1",
                 "KeyD": "ValueD1"
                 },
                {"KeyA": "ValueA2",
                 "KeyB": "ValueB2",
                 "KeyC": "ValueC2",
                 "KeyD": "ValueD2"
                 },
                {"KeyA": "ValueA3",
                 "KeyB": "ValueB3",
                 "KeyC": "ValueC3",
                 "KeyD": "ValueD3"
                 }
                ]

    UserRole = QtCore.Qt.UserRole

    ep = EntityPartLayout(window, UserRole, "KeyB", entities)

    ep.show()

    app.exec_()

# v Main - test                                                  ║
# ^ =============================================================╝
