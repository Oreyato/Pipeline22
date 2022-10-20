from manager.engine.base_engine import BaseEngine
from manager.engine.maya.maya_engine import MayaEngine
from manager.engine.os_pck.os_engine import OSEngine

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
    ### On va récupérer un critère et en fonction du critère, créer le bon engine -> suite de if en dur
    ### Pas très élégant mais pourra être ref. plus tard
    current_exe_path = sys.executable
    software_name = get_soft_name_from_path(current_exe_path)

    selected = BaseEngine

    if software_name == "python":
        selected = OSEngine
    elif software_name == "maya":
        selected = MayaEngine


    print(f'Selected engine: {selected}')

    return selected