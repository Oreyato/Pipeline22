import os

import lucidity
from manager import conf
from pathlib import Path

from manager.core.fs import file_search as fsea


# v Templates ===================================================╗
#                                                                ║

project_name = conf.projects.get("micromovie")

project_path = Path(conf.pipeline_path) / project_name

root = lucidity.Template('root', str(project_path).replace(os.sep, "/"))
resolver = {root.name: root}

general_template = lucidity.Template('general',
                                     '{@root}/{type}',
                                     template_resolver=resolver)

assets_template = lucidity.Template('asset',
                                    '{@root}/{type}/{category}/{name}/{task}/v{versionNb}/{name}_{state}.{ext}',
                                    template_resolver=resolver)
shots_template = lucidity.Template('shot',
                                   '{@root}/{type}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state}.{ext}',
                                   template_resolver=resolver)

#                                                                ║
# ^ Templates ===================================================╝
# v =============================================================╗
# v Parse and format functions                                   ║


def parse(pathP):
    """
    From a path, identify a template and parse data

    :return: data
    """
    path = pathP

    type = general_template.parse(path)

    if type.get('type') == 'assets':
        data = assets_template.parse(path)
        return data
    elif type.get('type') == 'shots':
        data = shots_template.parse(path)
        return data

    pass


def format(dataP):
    """
    Format data into a filepath, while identifying the correct template

    :return: filepath (string)
    """

    if dataP.get('type') == 'assets':
        path = assets_template.format(dataP)
        return path
    elif dataP.get('type') == 'shots':
        path = shots_template.format(dataP)
        return path

    pass


# v Parse and format functions                                   ║
# ^ =============================================================╝
# v =============================================================╗
# v Functions                                                    ║

# def update_templates(project_nameP):
#     new_project_name = conf.projects.get(project_nameP)
#
#     if project_name is not new_project_name:
#         project_name = new_project_name
#
#         project_path = Path(conf.pipeline_path) / project_name
#         print(f"Project path: {project_path}")
#
#         root = lucidity.Template('root', str(project_path).replace(os.sep, "/"))
#         resolver = {}
#         resolver[root.name] = root
#
#         general_template = lucidity.Template('general',
#                                              '{@root}/{type}',
#                                              template_resolver=resolver)
#
#         assets_template = lucidity.Template('asset',
#                                             '{@root}/{type}/{category}/{name}/{task}/v{versionNb}/{name}_{state}.{ext}',
#                                             template_resolver=resolver)
#         shots_template = lucidity.Template('shot',
#                                            '{@root}/{type}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state}.{ext}',
#                                            template_resolver=resolver)
#
#     pass


def get_entities(project_name, soft_programs=[""], selected_type='asset'):
    """
    Get files from the right project and right software along with the software they come from

    :param project_name: Give the production name, not the folder name
    :param filtersP: Filter what entities you want
    :return: yield a list
    """
    project_path = Path(conf.pipeline_path) / conf.projects.get(project_name)
    project_path = str(project_path).replace(os.sep, "/")

    entities = []

    for software in soft_programs:
        # Get files addresses
        files_addresses = list(fsea.get_file_addresses(project_path, software, selected_type))

        for file_address in files_addresses:
            # Parse data
            data = parse(str(file_address).replace(os.sep, "/"))
            # Create the data
            file_datas = [data, software]
            # Add the data to the data list
            entities.append(file_datas)

    return entities


# v Functions                                                    ║
# ^ =============================================================╝
# v =============================================================╗
# v Tests                                                        ║


if __name__ == '__main__':

    print(f'Entities: {get_entities("micromovie", ["Maya"])}')


# ^ Tests                                                        ║
# ^ =============================================================╝