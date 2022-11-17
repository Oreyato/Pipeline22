from pprint import pprint

import Qt as Qt
import Qt.QtCore as QtCore
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow, QHBoxLayout

from manager.ui.browser.objects_manager import ObjectsListManager
from manager.ui.browser.ep_lyt.entity_part_layout import EntityPartLayout
from manager import conf


class EntitiesListsManager(ObjectsListManager):
    def __init__(self, window_p, user_role_p, labels_p):
        # Call the parent constructor
        super(EntitiesListsManager, self).__init__()
        # Attributes init ======================
        self.__window = window_p
        self.__user_role = user_role_p
        self.__labels = labels_p

        self.__selected_lw_index = 0

        # Init
        self.init_lws_list()

    # v =============================================================╗
    # v List management methods                                      ║
    def init_lws_list(self):
        for label in self.__labels:
            epl = EntityPartLayout(self.__window, self.__user_role, label)
            self.append_obj(epl)

    def fill_list(self, index):
        """
        :type index: int
        """

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

    window = QMainWindow()
    UserRole = QtCore.Qt.UserRole

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

    layout = QHBoxLayout()

    labels = conf.table_labels.get('shots')
    lwm = EntitiesListsManager(window, UserRole, labels)

    for obj in lwm.objs:
        layout.addWidget(obj)

    window.setLayout(layout)

    window.show()

    app.exec_()

# v Main                                                         ║
# ^ =============================================================╝
