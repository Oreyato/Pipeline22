import os

class BaseEngine:

    def __init__(self):
        self.implement = ["Open"]

    # Override what the object returns when printed
    def __str__(self):
        return f"[{self.__class__.__name__}]"

    def open_file_from_path(file_path):
        print(f'Open file at: {file_path}')
        os.startfile(file_path)


# Create a "main" to test the class
if __name__ == "__main__":

    be = BaseEngine()
    print(be)
