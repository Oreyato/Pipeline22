import Qt as Qt
import Qt.QtCore as QtCore
from Qt.QtWidgets import QLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, QListWidget, QListWidgetItem
from Qt import QtWidgets, QtCompat

from manager import utils
from manager import conf

class EntityPartLayout(QtWidgets.QWidget):
    def __init__(self, parent_p, window_p, user_role_p, label_p, translated_label_p, entities_p=[]):
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
        self.__parent = parent_p
        self.__window = window_p
        self.__user_role = user_role_p
        self.__label = label_p
        self.__translated_label = translated_label_p
        self.__entities = entities_p

        self.__unique_entities = []

        self.__layout = None
        self.__list_widget = None

        self.__current_item = None
        self.__is_selected = False
        self.__is_active = False

        # Initialize
        self.init_layout()

        self.connect()

    # v =============================================================╗
    # v Methods                                                      ║
    # region Initialisations
    # v Initialisations =================
    def init_layout(self):
        # Prepare base name
        base_name = f'{self.__label}_ent_part'

        # v Create layout ================================================
        layout_name = f'{base_name}_layout'
        layout = QVBoxLayout()
        layout.setObjectName(layout_name)
        # ^ Create layout ================================================
        # v Create label =================================================
        label_name = f'{base_name}_label'
        entity_part_label = QLabel(self.__window)
        entity_part_label.setObjectName(label_name)
        entity_part_label.setText(self.__label)
        entity_part_label.setAlignment(QtCore.Qt.AlignCenter)
        # ^ Create label =================================================

        # Create list widget
        self.__list_widget = self.create_list_widget(base_name)
        self.fill_list()

        # Add the widgets inside the layouts
        layout.addWidget(entity_part_label)
        layout.addWidget(self.__list_widget)

        self.__layout = layout
        self.setLayout(layout)

    def create_list_widget(self, base_name_p):
        list_name = f'{base_name_p}_list'
        entity_part_list = QListWidget()
        entity_part_list.setObjectName(list_name)
        entity_part_list.setAlternatingRowColors(True)
        entity_part_list.setEnabled(False)

        return entity_part_list

    # endregion Initialisations
    # region Getters / Setters
    # v Getters / Setters ===============
    @property  # Works like a getter
    def layout(self):
        return self.__layout

    # If I wanted a setter, I would write it like that
    '''
    @layout.setter
    def layout(self, layout_p):
        self.__layout = layout_p
    '''

    @property
    def label(self):
        return self.__label

    @property
    def is_selected(self):
        return self.__is_selected

    @property
    def is_active(self):
        return self.__is_active

    @property
    def selected_item(self):
        return self.__selected_item

    def reset_is_active(self):
        self.__is_active = False

    def set_entities(self, entities_p):
        self.__entities = entities_p

        self.empty_list()
        self.fill_list()

    # endregion Getters / Setters
    # region Selected item
    # v Selected item ===================
    def select_item(self):
        self.__is_selected = True
        self.__is_active = True

        if len(self.__list_widget.selectedItems()) is not 0:
            print(f'Selected \"{self.__list_widget.selectedItems()[0].data(self.__user_role)}\"')

        self.__current_item = self.__list_widget.selectedItems()

        entity_str = self.__list_widget.selectedItems()[0].data(self.__user_role)
        entity = eval(entity_str)

        self.__parent.active_layout(entity)

    def connect(self):
        self.__list_widget.itemClicked.connect(self.select_item)

    # endregion Selected item
    # region Management
    # v Management ======================
    def __remove_entity_duplicates(self):
        # Remove entities duplicates ===========
        # Prepare the lists
        unique_values = []
        unique_entities = []

        # Browse the entities list
        for entity in self.__entities:
            # Keep track of the existence or not of a value
            exist = False

            dict_value = entity.get(self.__translated_label)

            # Browse the list that stores all known values
            for unique_value in unique_values:
                if dict_value == unique_value:
                    exist = True
            # If the value is not one of the already known values
            if not exist:
                unique_values.append(dict_value)
                unique_entities.append(entity)

        self.__unique_entities = unique_entities

    def __populate_widget_list(self):
        if len(self.__unique_entities) is not 0:
            self.__list_widget.setEnabled(True)

            for entity in self.__unique_entities:
                list_item = QListWidgetItem()
                print(entity)
                list_item.setData(self.__user_role, str(entity))
                list_item.setText(entity[self.__translated_label])
                print(f'{list_item.text()} | {list_item.data(self.__user_role)}')
                self.__list_widget.addItem(list_item)

    def fill_list(self):
        self.__remove_entity_duplicates()
        self.__populate_widget_list()

    def empty_list(self):
        self.__list_widget.clear()
        self.__list_widget.setEnabled(False)

    def close(self):
        pass

    # endregion Management
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

    from manager.ui.browser.entities_lists_manager import EntitiesListsManager

    ep = EntityPartLayout('EntitiesListManager instance', window, UserRole, "KeyB", "KeyB")
    ep.set_entities(entities)

    ep.show()

    app.exec_()

# v Main - test                                                  ║
# ^ =============================================================╝
