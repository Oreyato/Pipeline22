def clear_layout(layout):
    for i in reversed(range(layout.count())):
        widget_to_remove = layout.itemAt(i).widget
        layout.removeWidget(widget_to_remove)
        widget_to_remove.deleteLater()