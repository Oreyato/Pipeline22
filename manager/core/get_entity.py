import os
from pprint import pprint

from manager import conf
from pathlib import Path

from manager.core import resolver
from manager.core.fs import file_search as fs_search
from manager.core.sg_api import shotgun_search as sg_search


def get_entities(project_name, soft_programs=[""], selected_type='asset'):
    entities = []
    fs_entities = []
    sg_entities = []

    fs_entities = fs_get_entities(project_name, soft_programs, selected_type)
    sg_entities = sg_get_entities(project_name, soft_programs, selected_type)

    entities = fs_entities + sg_entities

    return entities


def fs_get_entities(project_name, soft_programs=[""], selected_type='asset'):
    """
    Get files from the right project and right software along with the software they come from

    :param project_name: Give the production name, not the folder name
    :param filtersP: Filter what entities you want
    :return: yield a list
    """
    project_path = Path(conf.pipeline_path) / conf.projects.get(project_name).get("name")
    project_path = str(project_path).replace(os.sep, "/")

    entities = []

    for software in soft_programs:
        # Get files addresses
        files_addresses = list(fs_search.get_file_addresses(project_path, software, selected_type))

        for file_address in files_addresses:
            # Parse data
            data = resolver.parse(str(file_address).replace(os.sep, "/"))
            # Create the data
            file_datas = [data, software]
            # Add the data to the data list
            entities.append(file_datas)

    return entities


def sg_get_entities(project_name, soft_programs=[""], selected_type='asset'):
    """
    Get files from the right project and right software along with the software they come from

    :param project_name: Give the production name, not the folder name
    :param filtersP: Filter what entities you want
    :return: yield a list
    """
    project_path = Path(conf.pipeline_path) / conf.projects.get(project_name).get("name")
    project_path = str(project_path).replace(os.sep, "/")

    entities = []

    for software in soft_programs:
        # Get files addresses
        files_addresses = list(fs_search.get_file_addresses(project_path, software, selected_type))

        for file_address in files_addresses:
            # Parse data
            data = resolver.parse(str(file_address).replace(os.sep, "/"))
            # Create the data
            file_datas = [data, software]
            # Add the data to the data list
            entities.append(file_datas)

    return entities

# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    pprint(get_entities("micromovie", ["Maya"], "shots"))

# ^ Tests                                                        ║
# ^ =============================================================╝