from pprint import pprint

from manager.ui.browser.objects_manager import ObjectsListManager
from manager.ui.browser.ep_lyt.entity_part_layout import EntityPartLayout


class EntitiesListsManager(ObjectsListManager):
    def __init__(self):
        # Call the parent constructor
        super(EntitiesListsManager, self).__init__()
        # Attributes init ======================
        self.selected_lw_index = 0

    # v =============================================================╗
    # v List management methods                                      ║
    def init_lws_list(self):
        pass

    def empty_list(self, index):
        """
        :type index: int
        """

        pass

    def fill_list(self, index):
        """
        :type index: int
        """

        pass

    # ^ List management methods                                      ║
    # ^ =============================================================╝
# v =============================================================╗
# v Main                                                         ║

if __name__ == "__main__":
    lwm = EntitiesListsManager()
    pprint(lwm.objs)

    pprint(lwm.max_index)

    lwm.append_obj("patrick")
    lwm.append_obj("jeanrené")
    pprint(lwm.objs)

    lwm.remove_obj_by_name("patrick")
    pprint(lwm.objs)

    lwm.get_obj_by_name("patrick")  # print "None" when an exception is raised
    lwm.get_obj_by_index(1)
    pprint(lwm.objs)

# v Main                                                         ║
# ^ =============================================================╝
