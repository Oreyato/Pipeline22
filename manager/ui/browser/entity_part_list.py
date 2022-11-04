import Qt as Qt
import Qt.QtCore as QtCore

from Qt.QtWidgets import QLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, QListWidget, QListWidgetItem

from Qt import QtWidgets, QtCompat


class EntityPartList(QtWidgets.QWidget):

    def __init__(self, label_p, window_p, user_role_p, entities_p=[]):
        # Call the parent constructor
        super(EntityPartList, self).__init__()
        # Set parameters
        self.label = label_p
        self.window = window_p
        self.user_role = user_role_p
        self.entities = entities_p

        # Initialize attributes
        self.layout = None
        self.list_widget = None

        # Initialize
        self.init_list()

        # Wait for inputs
        self.connect()

    def create_list_widget(self, base_name_p):
        # Prepare list widget name
        list_name = f'{base_name_p}_list'
        # Create list widget
        entity_part_list = QListWidget()
        # Modify list name
        entity_part_list.setObjectName(list_name)
        # Alternate row colors
        entity_part_list.setAlternatingRowColors(True)

        # Remove duplicates ====================
        # Prepare the lists
        unique_values = []
        unique_entities = []

        # Browse the entities list
        for entity in self.entities:
            # Keep track of the existence or not of a value
            exist = False
            # Get the entity value corresponding to the label
            dict_value = entity[self.label]

            # Browse the list that stores all known values
            for unique_value in unique_values:
                # If the value already exists
                if dict_value == unique_value:
                    exist = True
            # If the value is not one of the already known values
            if not exist:
                # Add it to the know values list
                unique_values.append(dict_value)
                # Add the entity to the unique entities list
                unique_entities.append(entity)

        # Populate the list ====================
        for entity in unique_entities:
            # Create the item to store in the list
            list_item = QListWidgetItem()
            # Store the entity inside
            list_item.setData(self.user_role, entity)
            # But show a value
            list_item.setText(entity[self.label])
            # Add the item in the list
            entity_part_list.addItem(list_item)

        return entity_part_list

    def init_list(self):
        # Prepare base name
        base_name = f'{self.label}_ent_part'

        # v Create layout ================================================
        # Prepare layout name
        layout_name = f'{base_name}_layout'
        # Create layout
        layout = QVBoxLayout()
        # Modify layout name
        layout.setObjectName(layout_name)
        # ^ Create layout ================================================
        # v Create label =================================================
        # Prepare label widget name
        label_name = f'{base_name}_label'
        # Create label widget
        entity_part_label = QLabel(self.window)
        # Modify label name
        entity_part_label.setObjectName(label_name)
        # Set its text
        entity_part_label.setText(self.label)
        # Set its alignment
        entity_part_label.setAlignment(QtCore.Qt.AlignCenter)
        # ^ Create label =================================================
        # Create list widget
        self.list_widget = self.create_list_widget(base_name)

        # Add the widgets inside the layouts
        layout.addWidget(entity_part_label)
        layout.addWidget(self.list_widget)

        # Update attribute value
        self.layout = layout
        # Update the current layout
        self.setLayout(layout)

    def get_layout(self):
        return self.layout

    def connect(self):
        self.list_widget.currentItemChanged.connect(self.get_selected_item)

    def get_selected_item(self):
        if len(self.list_widget.selectedItems()) is not 0:
            print(f'Selected \"{self.list_widget.selectedItems()[0].data(self.user_role)}\"')

        return self.list_widget.selectedItems()


# Create a "main" to Key the class
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

    ep = EntityPartList("KeyA", window, UserRole, entities)
    ep.show()

    app.exec_()
