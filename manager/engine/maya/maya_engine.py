from manager.engine.base_engine import BaseEngine


class MayaEngine(BaseEngine):

    def __init__(self):
        self.implement = []


# Create a "main" to test the class
if __name__ == "__main__":

    me = MayaEngine()
    print(me)

