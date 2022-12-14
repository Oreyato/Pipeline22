from pprint import pprint

from manager.core.search.base_search import BaseSearchSystem
from manager.core.search.sg_api import shotgrid

from manager.conf import conf_files as conf
from manager.core.search import resolver

class ShotgridSearchSystem(BaseSearchSystem):
    def __init__(self):
        super().__init__()

    def sg_files_to_entities(self, sg_files_p):
        entities = []

        pprint(sg_files_p)

        return entities

    @staticmethod
    def new_get_entities(filters_p):
        return []


if __name__ == "__main__":
    sss = ShotgridSearchSystem()
    print(sss)

    pprint(sss.get_entities("micromovie", ["Maya"], "Asset"))