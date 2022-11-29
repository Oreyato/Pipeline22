from pprint import pprint

from manager.core.search.base_search import BaseSearchSystem
from manager.core.search.sg_api import shotgrid

from manager.conf import conf_files as conf
from manager.core.search import resolver

class ShotgridSearchSystem(BaseSearchSystem):
    def __init__(self):
        pass

    def sg_files_to_entities(self, sg_files_p):
        entities = []

        pprint(sg_files_p)

        return entities

    @staticmethod
    def get_entities(self, project_name_p, soft_programs_p=[""], selected_type_p='asset'):
        """
        Get files from the right project and right software along with the software they come from

        :param project_name_p: Give the production name, not the folder name
        :param soft_programs_p: Select software
        :param selected_type_p: Select type
        :return: entities list
        """
        project_id = conf.projects.get(project_name_p).get("sg_id")

        sg_files = shotgrid.get_shotgun_files(project_id, selected_type_p)
        entities = self.sg_files_to_entities(sg_files)

        return entities


if __name__ == "__main__":
    sss = ShotgridSearchSystem()
    print(sss)

    pprint(sss.get_entities("micromovie", ["Maya"], "Asset"))