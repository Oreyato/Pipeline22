from manager.engine.base_engine import BaseEngine


class OSEngine(BaseEngine):

    def __init__(self):
        self.implement = []

    def open_file_from_path_and_software(file_path, software):
        print(f'Open {software} file at: {file_path}')

# Create a "main" to test the class
if __name__ == "__main__":

    oe = OSEngine()
    print(oe)

