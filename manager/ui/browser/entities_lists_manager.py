from pprint import pprint

import Qt as Qt
import Qt.QtCore as QtCore
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QWidget, QMainWindow, QHBoxLayout

from manager.ui.browser.objects_manager import ObjectsListManager
from manager.ui.browser.ep_lyt.entity_part_layout import EntityPartLayout
from manager import conf


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
    def __translate_label(self, label_p):
        tmp_label = conf.labels_to_lu_templates.get(label_p)

        if tmp_label is not None:
            return tmp_label
        else:
            return label_p

    def init_lws_list(self):
        for label in self.__labels:
            translated_label = self.__translate_label(label)

            epl = EntityPartLayout(self.__window, self.__user_role, label, translated_label)
            self.__parent_layout.addWidget(epl)
            self.append_obj(epl)

        self.fill_list(0, first_entities)

    def fill_list(self, index_p, entities_p):
        """
        :type index_p: int
        """
        self._objs[index_p].set_entities(entities_p)

        pass

    def empty_list(self, index):
        """
        :type index: int
        """

        pass

    # ^ List management methods                                      ║
    # ^ =============================================================╝
    # v =============================================================╗
    # v Entity part layout management                                ║
    def active_layout(self):
        is_active_index = self.__selected_lw_index

        # Parcourir la liste des lw de 0 au selected_lw_index
        for i, lw in enumerate(self.objs):
            # Si un lw est is_active
            if lw.get_is_active():
                # Mettre is_active_index à son index
                is_active_index = i
                # Mettre is_active de ce lw à False
                lw.reset_is_active()


        # Si is_active_index et selected_lw_index ont la même valeur
            # Mettre à jour le lw de droite
        # Sinon
            # Vider tous les lw jusqu'au lw à la position is_active_index

        pass

    # v Entity part layout management                                ║
    # ^ =============================================================╝
# v =============================================================╗
# v Main                                                         ║

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QWidget()
    UserRole = QtCore.Qt.UserRole

    test_asset_entities = [
        {'category': 'cameras', 'ext': 'ma', 'name': 'turn', 'state': 'work', 'task': 'rigging', 'type': 'assets', 'versionNb': '001'},
        {'category': 'props', 'ext': 'ma', 'name': 'dirt_car_01', 'state': 'work', 'task': 'modeling', 'type': 'assets', 'versionNb': '001'},
        {'category': 'props', 'ext': 'ma', 'name': 'dirt_car_01', 'state': 'work', 'task': 'modeling', 'type': 'assets', 'versionNb': '002'}
    ]
    first_entities = [
        {'category': 'cameras'},
        {'category': 'props'},
        {'category': 'props'}
    ]

    layout = QHBoxLayout()

    labels = conf.table_labels.get('assets')
    lwm = EntitiesListsManager(window, UserRole, layout, labels, first_entities)

    window.setLayout(layout)

    window.show()

    app.exec_()

# v Main                                                         ║
# ^ =============================================================╝
