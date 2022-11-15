from manager.core.base_search_system import BaseSearchSystem


class ShotgridSearchSystem(BaseSearchSystem):
    def __init__(self):
        pass

    def get_entities(self, project_name_p, soft_programs_p=[""], selected_type_p='asset'):
        pass


if __name__ == "__main__":
    sss = ShotgridSearchSystem()
    print(sss)