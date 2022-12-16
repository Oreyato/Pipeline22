from manager.engine.base_engine import BaseEngine


class HoudiniEngine(BaseEngine):

    def __init__(self):
        self.implement = ["Open", "Merge"]


# Create a "main" to test the class
if __name__ == "__main__":

    he = HoudiniEngine()
    print(he)

