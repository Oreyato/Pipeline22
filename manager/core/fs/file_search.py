from manager import conf
from pathlib import Path

# v =============================================================╗
# v Create data list                                             ║

# From pipeline_path, get all Maya and Houdini files and store them in a list
# along with their type (Maya or Houdini file) and path (from pipeline_path)


def init_data_list(project_name, soft_programs=[""]):
    """
    Get files from the right project and right software along with the software they come from and their path

    :param project_name: Give the production name, not the folder name
    :param soft_programs: Needs a list of software
    :return: yield a list
    """
    project_path = Path(conf.pipeline_path) / conf.projects.get(project_name)

    data_list = []
    soft_files = []

    for software in soft_programs:
        # Get files addresses
        files_addresses = list(get_file_addresses(project_path, software))

        for file_address in files_addresses:
            # Get file name
            file_name = get_file_name_from_path(file_address)
            # Create the data
            file_datas = [file_name, software, file_address]
            # Add the data to the data list
            data_list.append(file_datas)

    return data_list


def get_file_addresses(project_path, software):
    """
    Get files addresses from the right project and right software

    :param project_path: Path to the folder containing the project
    :param software: Needs a software
    :return: yield a generator
    """
    generators = []
    extensions = []

    # Get selected software extensions
    extensions.extend(conf.software_programs.get(software))
    # print(f"Allowed extensions: {extensions}")

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
    # Convert the path to a string
    f_path_str = str(f_path)
    # Split the path
    split_path = f_path_str.split("\\")
    # Get the last element of the list
    file_name = split_path[len(split_path) - 1]

    return file_name

# ^ Create data list                                             ║
# ^ =============================================================╝
# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    data_list = list(init_data_list("micromovie", ["Maya"]))

# ^ Tests                                                        ║
# ^ =============================================================╝