from manager.engine.base_engine import BaseEngine
import maya.cmds as cmds

class MayaEngine(BaseEngine):

    def __init__(self):
        self.implement = ["Open", "Reference", "Import"]

    def open_file_from_path(file_path):
        print(f'Open file from Maya at: {file_path}')
        cmds.file(file_path, o=True)


# Create a "main" to test the class
if __name__ == "__main__":

    me = MayaEngine()
    print(me)
    print(cmds.ls())


