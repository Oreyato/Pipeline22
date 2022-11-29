import os
from pathlib import Path
from pprint import pprint

from manager.core.search.base_search import BaseSearchSystem
from manager.core.search.fs import file_search as fs_search

from manager.conf import conf_files as conf
from manager.core.search import resolver


class FilesystemSearchSystem(BaseSearchSystem):
    @staticmethod
    def get_entities(project_name_p, soft_programs_p=[""], selected_type_p='asset'):
        """
        Get files from the right project and right software along with the software they come from

        :param project_name_p: Give the production name, not the folder name
        :param soft_programs_p: Select software
        :param selected_type_p: Select type
        :return: entities list
        """
        project_path = Path(conf.pipeline_path) / conf.projects.get(project_name_p).get("name")
        project_path = str(project_path).replace(os.sep, "/")

        entities = []

        for software in soft_programs_p:
            # Get files addresses
            files_addresses = list(fs_search.get_file_addresses(project_path, software, selected_type_p))

            for file_address in files_addresses:
                # Parse data
                data = resolver.parse(str(file_address).replace(os.sep, "/"))
                # Create the data
                file_datas = [data, software]
                # Add the data to the data list
                entities.append(file_datas)

        return entities

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
            # Get files addresses
            files_addresses = list(fs_search.new_get_file_addresses(software, filters_p))

            for file_address in files_addresses:
                str_f_address = str(file_address).replace(os.sep, "/")
                data = {
                    'soft programs': [software],
                    'project': current_project
                }

                entity = resolver.parse(str_f_address)
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

    entities = FilesystemSearchSystem.new_get_entities(filters)

    pprint(entities)
