import os
import pathlib
from pprint import pprint

from manager import conf
from pathlib import Path


# v =============================================================╗
# v Create data list                                             ║

# From project_root, get all Maya and Houdini files and store them in a list
# along with their type (Maya or Houdini file) and path (from project_root)

def init_data_list(project_name, soft_programs=[""]):
    """
    Get files from the right project and right software along with the software they come from and their path

    :param project_name: Give the production name, not the folder name
    :param soft_programs: Needs a list of software
    :return: yield a list
    """
    project_path = Path(conf.project_root) / conf.projects.get(project_name).get("name")

    data_list = []
    soft_files = []

    for software in soft_programs:
        # Get files path
        files_path = list(get_file_path(project_path, software))

        for file_path in files_path:
            # Get file name
            file_name = get_file_name_from_path(file_path)
            # Create the data
            file_datas = [file_name, software, file_path]
            # Add the data to the data list
            data_list.append(file_datas)

    return data_list


def get_file_path(project_path, software, selected_type='asset'):
    """
    Get files path from the right project and right software

    :param project_path: Path to the folder containing the project
    :param software: Needs a software
    :return: yield a generator
    """
    generators = []
    extensions = []

    # Get selected software extensions
    extensions.extend(conf.software_list.get(software))
    # print(f"Allowed extensions: {extensions}")

    # Get files that have one of the allowed extensions
    # ==v== CAN EASILY BE IMPROVED ==v==
    for ext in extensions:
        if selected_type == conf.types[1]:
            asset_pattern = conf.asset_file_pattern.format(ext=ext)
            found = Path(project_path).rglob(asset_pattern)
            generators.append(found)
        elif selected_type == conf.types[2]:
            shot_pattern = conf.shot_file_pattern.format(ext=ext)
            found = Path(project_path).rglob(shot_pattern)
            generators.append(found)

    for g in generators:
        for f in g:
            yield f


def new_get_file_path(software_p, filters_p):
    """
    Get files path from the right project and right software

    :param software_p: Selected software
    :param filters_p: Dictionary
    :return: yield a generator
    """
    generators = []
    extensions = []

    # Get project path
    project_name = filters_p.get('project')
    project_path = Path(conf.project_root) / conf.projects.get(project_name).get("name")
    project_path = str(project_path).replace(os.sep, "/")

    # Get selected software extensions
    extensions.extend(conf.software_list.get(software_p))

    selected_type = filters_p.get('type')

    # v Prepare the rglob parameter ==================================
    # Shorten the list
    filters_p.pop('project')
    filters_p.pop('soft programs')
    shorten_filters = list(filters_p.values())
    pprint(shorten_filters)
    shorten_filters.append('*')

    # pattern = '{type}/{category}/{name}/{soft_programs}'
    # rglob_param = pattern.format(**filters_p)
    # pprint(rglob_param)

    rglob_param = '/'.join(shorten_filters)
    pprint(rglob_param)

    # ^ Prepare the rglob parameter ==================================

    # Get files that have one of the allowed extensions
    # ==v== CAN EASILY BE IMPROVED ==v==
    # for ext in extensions:

    #todo SOLVE RGLOB ISSUE
    found = Path(project_path).rglob(rglob_param)
    generators.append(found)

    for g in generators:
        for f in g:
            yield f


def get_file_name_from_path(f_path):
    path = str(f_path).replace(os.sep, "/")
    f_name = pathlib.PurePosixPath(path).stem

    return f_name

# ^ Create data list                                             ║
# ^ =============================================================╝
# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    from manager import utils
    #utils.init_lucidity_templates('MMOVIE', 'assets')

    filters = {
        'project': 'micromovie',
        'type': 'assets',
        'soft_programs': ['Maya'],
        'category': 'props',
        'name': 'dirt_car_01'
    }

    # file = "D:\TD4\Paul\Pipeline\PyProject\Pipeline22\README.md"
    # path = str(file).replace(os.sep, "/")
    # file_name = pathlib.PurePosixPath(path).stem
    # print(file_name)

    # pattern = '{type}/{category}/{name}/{soft_programs}'
    # rglob_param = pattern.format(**filters_p)
    # pprint(rglob_param)

   #  path = list(new_get_file_path('Maya', filters))
    #pprint(path)

# ^ Tests                                                        ║
# ^ =============================================================╝
