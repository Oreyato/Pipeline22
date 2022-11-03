import Qt as Qt

from Qt import QtWidgets
from Qt.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget


class EntityPartList:

    def __init__(self, label_p, entity_p):
        self.label = label_p
        self.entity = entity_p

    def init_list(self):
        # Create layout
        layout = QVBoxLayout()
        # v Create label =================================================
        # Prepare label widget name
        label_name = f'{self.label}'
        # Create label widget
        entity_part_label = QLabel()
        # Set its text
        entity_part_label.setText(self.label)
        # Set its alignment
        entity_part_label.setAlignmnent(Qt.AlignCenter)
        # ^ ==============================================================
        # Create list widget
        entity_part_list = QListWidget()

        # Add the widgets inside the layout
        layout.addWidget(entity_part_label)
        layout.addWidget()

        pass


# Create a "main" to test the class
if __name__ == "__main__":

    ep = EntityPartList("label", "entity")
    print(ep)