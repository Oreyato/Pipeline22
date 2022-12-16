from manager.engine.base_engine import BaseEngine

import sys


def get_soft_name_from_path(f_path):
    # split the path
    split_path = f_path.split("\\")
    # get the last element of the list
    file_name_and_ext = split_path[len(split_path) - 1]

    # split the name
    split_name = file_name_and_ext.split(".")
    # get the first element of the list
    file_name = split_name[0]

    return file_name


def get():
    """
    Returns engine depending on the context

    :return:
    """
    current_exe_path = sys.executable
    software_name = get_soft_name_from_path(current_exe_path)

    selected = BaseEngine

    if software_name == "python":
        from manager.engine.os_pck.os_engine import OSEngine
        selected = OSEngine()

    elif software_name == "maya":
        from manager.engine.maya.maya_engine import MayaEngine
        selected = MayaEngine()

    elif software_name == "houdini":
        from manager.engine.houdini.houdini_engine import HoudiniEngine
        selected = HoudiniEngine()

    print(f'Selected engine: {selected}')

    return selected