import os
from pathlib import Path
from pprint import pprint

from manager.core.search.base_search import BaseSearchSystem
from manager.core.search.fs import fs_utils as file_search

from manager.conf import conf_files as conf
from manager.core.search import resolver

from manager.utils.decorators import execution_time


class FilesystemSearch(BaseSearchSystem):
    def __init__(self):
        super().__init__()

    @staticmethod
    def new_get_entities(filters_p={}):
        """
        Get files from the right project and right software along with the software they come from

        :param filters_p: dictionary working as a filter
        :return: entities list
        """
        entities = []

        soft_programs = filters_p.get('soft programs')
        current_project = filters_p.get('project')

        for software in soft_programs:
            # Get files path
            files_path = list(file_search.new_get_file_path(software, filters_p))

            for file_path in files_path:
                str_f_path = str(file_path).replace(os.sep, "/")
                data = {
                    'soft programs': [software],
                    'project': current_project
                }

                entity = resolver.parse(str_f_path)
                if len(entity.keys()) != 0:
                    data.update(entity)
                    entities.append(data)

        return entities


if __name__ == "__main__":
    from manager import utils
    utils.init_lucidity_templates('MMOVIE', 'assets')

    filters = {
        'project': 'micromovie',
        'type': 'assets',
        'soft programs': ['Maya'],
        'category': 'props',
        'name': 'dirt_car_01'
    }

    entities = FilesystemSearch.new_get_entities(filters)

    pprint(entities)
