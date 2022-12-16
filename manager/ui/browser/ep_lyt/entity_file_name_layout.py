import Qt as Qt
import Qt.QtCore as QtCore
from Qt.QtWidgets import QLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, QListWidget, QListWidgetItem
from Qt import QtWidgets, QtCompat

from manager import utils
from manager import conf

from manager.ui.browser.ep_lyt.entity_part_layout import EntityPartLayout

class EntityFileNameLayout(EntityPartLayout):
    def __init__(self, parent_p, window_p, user_role_p, label_p, translated_label_p, entity_p=[]):
        super(EntityFileNameLayout, self).__init__(parent_p, window_p, user_role_p, label_p, translated_label_p, entity_p)

    def fill_list(self):
        self._unique_entities = self._entities
        self._populate_widget_list()

    def _populate_widget_list(self):
        if len(self._unique_entities) != 0:
            self._list_widget.setEnabled(True)

            for entity in self._unique_entities:
                list_item = QListWidgetItem()
                list_item.setData(self._user_role, str(entity))
                if entity['type'] == 'assets':
                    list_item.setText(f"{entity['name']}_{entity['state']}.{entity['ext']}")
                else:
                    list_item.setText(f"{entity['shNb']}_{entity['state']}.{entity['ext']}")
                self._list_widget.addItem(list_item)

            print('Populated widget list')

    def select_item(self):
        self._is_selected = True
        self._is_active = True

        if len(self._list_widget.selectedItems()) != 0:
            print("=== SELECTED ===")
            print(f'{self._list_widget.selectedItems()[0].data(self._user_role)}')

        self._current_item = self._list_widget.selectedItems()

        entity_str = self._list_widget.selectedItems()[0].data(self._user_role)
        entity = eval(entity_str)

        # self._parent.active_layout(entity)


if __name__ == "__main__":
    pass
    # app = QtWidgets.QApplication()
    #
    # window = QMainWindow()
    #
    # entities = [
    #     {
    #      'soft programs': ['Maya'],
    #      'project': 'micromovie',
    #      'category': 'props',
    #      'ext': 'mb',
    #      'name': 'dirt_car_01',
    #      'state': 'publish',
    #      'task': 'modeling',
    #      'type': 'assets',
    #      'versionNb': 'v001'
    #      },
    #     {
    #      'soft programs': ['Maya'],
    #      'project': 'micromovie',
    #      'category': 'props',
    #      'ext': 'ma',
    #      'name': 'dirt_car_01',
    #      'state': 'work',
    #      'task': 'modeling',
    #      'type': 'assets',
    #      'versionNb': 'v001'
    #      }
    # ]
    #
    # UserRole = QtCore.Qt.UserRole
    #
    # from manager.ui.browser.entities_lists_manager import EntitiesListsManager
    #
    # ep = EntityFileNameLayout('EntitiesListManager instance', window, UserRole, "File name", "name")
    # ep.set_entities(entities)
    #
    # ep.show()
    #
    # app.exec_()

# v Main - test                                                  ║
# ^ =============================================================╝
