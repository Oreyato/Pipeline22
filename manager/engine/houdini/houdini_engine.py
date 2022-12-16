from manager.engine.base_engine import BaseEngine
from manager import conf

class HoudiniEngine(BaseEngine):

    def __init__(self):
        self.implement = ["Open", "Merge"]

        conf.altRowColors = False


# Create a "main" to test the class
if __name__ == "__main__":

    he = HoudiniEngine()
    print(he)

