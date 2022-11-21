# Works as a C++ interface
class BaseSearchSystem:
    def __init__(self):
        pass

    def __str__(self):
        return f"[{self.__class__.__name__}]"

    @staticmethod
    def get_entities(project_name_p, soft_programs_p=[""], selected_type_p='asset'):
        pass

    @staticmethod
    def new_get_entities(filters_p):
        pass


if __name__ == "__main__":
    bss = BaseSearchSystem()
    print(bss)
