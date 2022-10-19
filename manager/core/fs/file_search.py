from manager import conf
from pathlib import Path

# v =============================================================╗
# v Create data list                                             ║

# From pipeline_path, get all Maya and Houdini files and store them in a list
# along with their type (Maya or Houdini file) and path (from pipeline_path)

def get_files(project_name, software_programs):
    project_path = Path(conf.pipeline_path) / conf.projects.get(project_name)
    generators = []





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
    # find the correct path ==============================
    # remove the extension ===============
    # split the path
    split_path = f_path.split("\\")
    # get the last element of the list
    file_name = split_path[len(split_path) - 1]

    return file_name


# ^ Create data list                                             ║
# ^ =============================================================╝