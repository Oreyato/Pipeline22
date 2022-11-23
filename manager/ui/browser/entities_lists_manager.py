from pprint import pprint

import Qt as Qt
import Qt.QtCore as QtCore
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QWidget, QMainWindow, QHBoxLayout

from manager.ui.browser.objects_manager import ObjectsListManager
from manager.ui.browser.ep_lyt.entity_part_layout import EntityPartLayout
from manager import conf

from manager.core.search import entities

class EntitiesListsManager(ObjectsListManager):
    def __init__(self, window_p, user_role_p, parent_layout_p, labels_p, first_entities_p):
        # Call the parent constructor
        super(EntitiesListsManager, self).__init__()
        # Attributes init ======================
        self.__window = window_p
        self.__user_role = user_role_p
        self.__parent_layout = parent_layout_p
        self.__labels = labels_p
        self.__f_entities = first_entities_p

        self.__selected_lw_index = 0

        # Init
        self.init_lws_list()

    # v =============================================================╗
    # v List management methods                                      ║
    def init_lws_list(self):
        for label in self.__labels:
            translated_label = self.__translate_label(label)

            epl = EntityPartLayout(self, self.__window, self.__user_role, label, translated_label)
            self.__parent_layout.addWidget(epl)
            self.append_obj(epl)

        self.fill_list(0, self.__f_entities)

    def fill_list(self, index_p, entities_p):
        """
        :type index_p: int
        :param index_p:
        :param entities_p:
        """
        self._objs[index_p].set_entities(entities_p)

        pass

    def empty_list(self, index_p):
        """
        :type index_p: int
        """
        self._objs[index_p].empty_list()

    # ^ List management methods                                      ║
    # ^ =============================================================╝
    # v =============================================================╗
    # v Entity part layout management                                ║
    def __sort_entities(self, entities_p):
        sorted_entities = []

        for entity in entities_p:
            entity_type = entity.get('type')
            sorted_entity = {
                'soft programs': entity.get('soft programs'),
                'project': entity.get('project')
            }

            for table_key in conf.tables_order.get(entity_type):
                for key in entity.keys():
                    if key == table_key:
                        sorted_entity.update({key: entity.get(key)})

            sorted_entities.append(sorted_entity)

        return sorted_entities

    def active_layout(self, entity_p):
        active_index = self.__selected_lw_index

        # Browse the list widget list and search for the active lw
        for i, lw in enumerate(self.objs):
            if lw.is_active:
                active_index = i
                lw.reset_is_active()

        # If the active lw is not the right-most one
        if active_index is not self.__selected_lw_index:
            # Empty all lw to the active_index
            for i in range(active_index + 1, self.__selected_lw_index + 1):
                self.objs[i].empty_list()

        # Update lw to the right
        # Get filtered entity
        entities_to_sort = entities.new_get_entities(entity_p)

        # Update right widget
        self.fill_list(active_index + 1, self.__sort_entities(entities_to_sort))
        self.__selected_lw_index = active_index + 1


    # v Entity part layout management                                ║
    # ^ =============================================================╝
    # v =============================================================╗
    # v Utils                                                        ║
    @staticmethod
    def __translate_label(label_p):
        tmp_label = conf.labels_to_lu_templates.get(label_p)

        if tmp_label is not None:
            return tmp_label
        else:
            return label_p

    # v Utils                                                        ║
    # ^ =============================================================╝
# v =============================================================╗
# v Main                                                         ║


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QWidget()
    UserRole = QtCore.Qt.UserRole

    from manager import utils
    utils.init_lucidity_templates('MMOVIE', 'assets')

    test_asset_entities = [
        {'category': 'cameras', 'ext': 'ma', 'name': 'turn', 'state': 'work', 'task': 'rigging', 'type': 'assets', 'versionNb': '001'},
        {'category': 'props', 'ext': 'ma', 'name': 'dirt_car_01', 'state': 'work', 'task': 'modeling', 'type': 'assets', 'versionNb': '001'},
        {'category': 'props', 'ext': 'ma', 'name': 'dirt_car_01', 'state': 'work', 'task': 'modeling', 'type': 'assets', 'versionNb': '002'},
        {'category': 'props', 'ext': 'ma', 'name': 'dirt_car_01', 'state': 'work', 'task': 'modeling', 'type': 'assets', 'versionNb': '003'}
    ]
    first_entities = [
        {'soft programs': ['Maya'], 'project': 'micromovie', 'type': 'assets', 'category': 'cameras'},
        {'soft programs': ['Maya'], 'project': 'micromovie', 'type': 'assets', 'category': 'props'},
        {'soft programs': ['Maya'], 'project': 'micromovie', 'type': 'assets', 'category': 'props'}
    ]

    layout = QHBoxLayout()

    labels = conf.table_labels.get('assets')
    lwm = EntitiesListsManager(window, UserRole, layout, labels, first_entities)

    window.setLayout(layout)

    window.show()

    app.exec_()

# v Main                                                         ║
# ^ =============================================================╝
