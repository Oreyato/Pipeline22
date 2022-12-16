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
        self._parent = parent_p
        self._window = window_p
        self._user_role = user_role_p
        self._label = label_p
        self._translated_label = translated_label_p
        self._entities = entities_p

        self._unique_entities = []

        self._layout = None
        self._list_widget = None

        self._current_item = None
        self._is_selected = False
        self._is_active = False

        # Initialize
        self.init_layout()

        self._connect()

    # v =============================================================╗
    # v Methods                                                      ║
    # region Initialisations
    # v Initialisations =================
    def init_layout(self):
        # Prepare base name
        base_name = f'{self._label}_ent_part'

        # v Create layout ================================================
        layout_name = f'{base_name}_layout'
        layout = QVBoxLayout()
        layout.setObjectName(layout_name)
        # ^ Create layout ================================================
        # v Create label =================================================
        label_name = f'{base_name}_label'
        entity_part_label = QLabel()
        entity_part_label.setObjectName(label_name)
        entity_part_label.setText(self._label)
        entity_part_label.setAlignment(QtCore.Qt.AlignCenter)
        # ^ Create label =================================================

        # Create list widget
        self._list_widget = self.create_list_widget(base_name)
        self.fill_list()

        # Add the widgets inside the layouts
        layout.addWidget(entity_part_label)
        layout.addWidget(self._list_widget)

        self._layout = layout
        self.setLayout(layout)

    def create_list_widget(self, base_name_p):
        list_name = f'{base_name_p}_list'
        entity_part_list = QListWidget()
        entity_part_list.setObjectName(list_name)
        entity_part_list.setAlternatingRowColors(conf.altRowColors)
        entity_part_list.setEnabled(False)
        # entity_part_list.setResizeMode(QListWidget.ResizeMode.Adjust)
        # entity_part_list.setWordWrap(False)
        # entity_part_list.setAutoScroll(True)
        entity_part_list.adjustSize()
        entity_part_list.setSizeAdjustPolicy(QListWidget.AdjustToContents)
        #entity_part_list.setWrapping(True)

        return entity_part_list

    # endregion Initialisations
    # region Getters / Setters
    # v Getters / Setters ===============
    @property  # Works like a getter
    def layout(self):
        return self._layout

    # If I wanted a setter, I would write it like that
    '''
    @layout.setter
    def layout(self, layout_p):
        self._layout = layout_p
    '''

    @property
    def label(self):
        return self._label

    @property
    def is_selected(self):
        return self._is_selected

    @property
    def is_active(self):
        return self._is_active

    @property
    def selected_item(self):
        return self._selected_item

    def reset_is_active(self):
        self._is_active = False

    def set_entities(self, entities_p):
        self._entities = entities_p

        self.empty_list()
        self.fill_list()

    # endregion Getters / Setters
    # region Selected item
    # v Selected item ===================
    def select_item(self):
        self._is_selected = True
        self._is_active = True

        if len(self._list_widget.selectedItems()) != 0:
            print(f'Selected \"{self._list_widget.selectedItems()[0].data(self._user_role)}\"')

        self._current_item = self._list_widget.selectedItems()

        entity_str = self._list_widget.selectedItems()[0].data(self._user_role)
        entity = eval(entity_str)

        self._parent.active_layout(entity)

    def _connect(self):
        self._list_widget.itemClicked.connect(self.select_item)

    # endregion Selected item
    # region Management
    # v Management ======================
    def _remove_entity_duplicates(self):
        # Remove entities duplicates ===========
        # Prepare the lists
        unique_values = []
        unique_entities = []

        # Browse the entities list
        for entity in self._entities:
            # Keep track of the existence or not of a value
            exist = False

            dict_value = entity.get(self._translated_label)

            # Browse the list that stores all known values
            for unique_value in unique_values:
                if dict_value == unique_value:
                    exist = True
            # If the value is not one of the already known values
            if not exist:
                unique_values.append(dict_value)
                unique_entities.append(entity)

        self._unique_entities = unique_entities

    def _populate_widget_list(self):
        if len(self._unique_entities) != 0:
            self._list_widget.setEnabled(True)

            for entity in self._unique_entities:
                list_item = QListWidgetItem()
                list_item.setData(self._user_role, str(entity))
                list_item.setText(entity[self._translated_label])
                self._list_widget.addItem(list_item)

            print('Populated widget list')

    def fill_list(self):
        self._remove_entity_duplicates()
        self._populate_widget_list()

    def empty_list(self):
        self._list_widget.clear()
        self._list_widget.setEnabled(False)

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
