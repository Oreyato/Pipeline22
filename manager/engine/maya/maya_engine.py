from manager.engine.base_engine import BaseEngine


class MayaEngine(BaseEngine):

    def __init__(self):
        self.implement = []

    # Override what the object returns when printed
    def __str__(self):
        return f"[{__class__.__name__}]"


# Create a "main" to test the class
if __name__ == "__main__":

    me = MayaEngine()
    print(me)

