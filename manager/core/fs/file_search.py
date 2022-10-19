from manager import conf
from pathlib import Path

# v =============================================================╗
# v Create data list                                             ║

# From pipeline_path, get all Maya and Houdini files and store them in a list
# along with their type (Maya or Houdini file) and path (from pipeline_path)
def init_data_list(project_name, soft_keys_list = ["Maya"]):
    """
    Get files from the right project and right software along with the software they come from and their path

    :param project_name: Give the production name, not the folder name
    :param soft_keys_list: Needs a list of software
    :return: yield a list
    """
    data_list = []

    ma_datas = init_data_from_ext_and_soft("*.ma", "Maya")
    mb_datas = init_data_from_ext_and_soft("*.mb", "Maya")
    hipnc_datas = init_data_from_ext_and_soft("*.hipnc", "Houdini")


    return data_list


def get_file_addresses(project_name, soft_keys_list = ["Maya"]):
    """
    Get files addresses from the right project and right software

    :param project_name: Give the production name, not the folder name
    :param soft_keys_list: Needs a list of software
    :return: yield a generator
    """
    project_path = Path(conf.pipeline_path) / conf.projects.get(project_name)
    print(f"Project path: {project_path}")
    generators = []
    extensions = []

    # Get selected software extensions
    for soft_keys in soft_keys_list:
        extensions.extend(conf.software_programs.get(soft_keys))

    print(f"Allowed extensions: {extensions}")

    # Get files that have one of the allowed extensions
    for ext in extensions:
        shot_pattern = conf.shot_file_pattern.format(ext=ext)
        found = Path(project_path).rglob(shot_pattern)
        generators.append(found)
        asset_pattern = conf.asset_file_pattern.format(ext=ext)
        found = Path(project_path).rglob(asset_pattern)
        generators.append(found)

    for g in generators:
        for f in g:
            yield f


def get_file_name_from_path(f_path):
    # split the path
    split_path = f_path.split("\\")
    # get the last element of the list
    file_name = split_path[len(split_path) - 1]

    return file_name


# v To ref =============================================
def init_data_list():
    ma_datas = init_data_from_ext_and_soft("*.ma", "Maya")
    mb_datas = init_data_from_ext_and_soft("*.mb", "Maya")
    hipnc_datas = init_data_from_ext_and_soft("*.hipnc", "Houdini")

    data_list = [ma_datas, mb_datas, hipnc_datas]

    return data_list


def init_data_from_ext_and_soft(extension, software):
    # Get paths from extension
    paths_list = get_path_from_extension(extension)
    data_list = []

    # Get according names and set right software name
    for path in paths_list:
        file_name = get_file_name_from_path(path)
        data_list.append([file_name, software, path])

    return data_list


def get_path_from_extension(extension):
    paths_list = []

    project_path = Path(conf.pipeline_path) / conf.projects.get('micromovie')

    for item in project_path.rglob(extension):
        paths_list.append(str(item))

    return paths_list


def get_file_name_from_path(f_path):
    # split the path
    split_path = f_path.split("\\")
    # get the last element of the list
    file_name = split_path[len(split_path) - 1]

    return file_name


# ^ To ref =============================================

# ^ Create data list                                             ║
# ^ =============================================================╝
# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    data_list = list(get_file_addresses("micromovie", ["Maya"]))
    print(data_list)

# ^ Tests                                                        ║
# ^ =============================================================╝