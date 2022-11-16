from pprint import pprint

from manager.ui.browser.objects_manager import ObjectsListManager


class ListWidgetsManager(ObjectsListManager):
    def __init__(self):
        # Call the parent constructor
        super().__init__()


    # v =============================================================╗
    # v Widgets management methods                                   ║



    # ^ Widgets management methods                                   ║
    # ^ =============================================================╝

# v =============================================================╗
# v Main                                                         ║
if __name__ == "__main__":
    lwm = ListWidgetsManager()
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
