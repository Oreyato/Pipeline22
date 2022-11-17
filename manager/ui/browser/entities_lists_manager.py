from pprint import pprint

import Qt as Qt
import Qt.QtCore as QtCore
from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QMainWindow

from manager.ui.browser.objects_manager import ObjectsListManager
from manager.ui.browser.ep_lyt.entity_part_layout import EntityPartLayout


class EntitiesListsManager(ObjectsListManager):
    def __init__(self):
        # Call the parent constructor
        super(EntitiesListsManager, self).__init__()
        # Attributes init ======================
        self.selected_lw_index = 0

        self.objs = []

    # v =============================================================╗
    # v List management methods                                      ║
    def init_lws_list(self):
        pass

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
        is_active_index = self.selected_lw_index

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

    # v List widgets creation ========================================
    # List widget 0 ========================
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

    epl = EntityPartLayout(window, UserRole, "KeyB", entities)
    # ^ List widgets creation ========================================

    lwm = EntitiesListsManager()
    pprint(lwm.objs)

    pprint(lwm.max_index)

    lwm.append_obj(epl)
    pprint(lwm.objs)

    lwm.remove_obj_by_name("patrick")
    pprint(lwm.objs)

    lwm.get_obj_by_name("patrick")  # print "None" when an exception is raised
    lwm.get_obj_by_index(1)
    pprint(lwm.objs)

    epl.show()

    app.exec_()

# v Main                                                         ║
# ^ =============================================================╝
