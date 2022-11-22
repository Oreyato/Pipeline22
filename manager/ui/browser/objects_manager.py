from pprint import pprint

from manager.utils.exception import PipelineException


class ObjectsListManager:
    def __init__(self):
        # Attributes init ======================
        # Create list widgets list
        self._objs = []

        self._max_index = -1

    # v =============================================================╗
    # v Objects management methods                                   ║
    def append_obj(self, obj):
        self._objs.append(obj)
        self._max_index = self._max_index + 1

    def insert_obj(self, obj, index):
        self._objs.insert(index, obj)
        self._max_index = self._max_index + 1

    def remove_obj_by_name(self, obj_name):
        obj = self.get_obj_by_name(obj_name)

        if obj is None:
            print("remove_obj_by_name() - Please enter a proper name")
            pass
        else:
            self._objs.remove(obj)
            self._max_index = self._max_index - 1

    def pop_obj(self, index):
        if PipelineException.index_test(self._max_index, index, "pop_obj") != -1:
            self._objs.pop(index)

    # ^ Objects management methods                                   ║
    # ^ =============================================================╝
    # v =============================================================╗
    # v Getters setters                                              ║
    @property
    def objs(self):
        return self._objs

    @property
    def max_index(self):
        return self._max_index

    # v Getters setters                                              ║
    # ^ =============================================================╝
    # v =============================================================╗
    # v Utils methods                                                ║
    def obj_index(self, obj_name):
        """
        :type obj_name: string
        :rtype: int
        """
        try:
            index = self._objs.index(obj_name)
            return index
        except ValueError as e:
            print(f"Pipeline exception - obj_index(): {e}")
            return -1

    def get_obj_by_index(self, index):
        """
        :type index: int
        :returns: list widget
        """
        if PipelineException.index_test(self._max_index, index, "get_obj_by_index") != -1:
            obj = self._objs[index]
            return obj

    def get_obj_by_name(self, obj_name):
        """
        :type obj_name: string
        :return: list widget
        """
        index = self.obj_index(obj_name)

        try:
            if index == -1:
                raise PipelineException("wrong index")
            else:
                obj = self._objs[index]
                return obj
        except PipelineException as e:
            print(f"Pipeline exception - get_obj_by_name(): {e}")

    # v Utils methods                                                ║
    # ^ =============================================================╝

# v =============================================================╗
# v Main                                                         ║
if __name__ == "__main__":
    # Create list manager
    om = ObjectsListManager()
    pprint(om.objs)

    om.append_obj("patrick")
    om.append_obj("jeanrené")
    pprint(om.objs)

    om.remove_obj_by_name("patrick")
    pprint(om.objs)

    om.get_obj_by_name("patrick")  # print "None" when an exception is raised
    om.get_obj_by_index(1)
    pprint(om.objs)

# v Main                                                         ║
# ^ =============================================================╝
