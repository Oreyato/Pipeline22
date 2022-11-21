import lucidity
import os
from pathlib import Path
from pprint import pprint

from manager import conf


def clear_layout(layout):
    for i in reversed(range(layout.count())):
        widget_to_remove = layout.itemAt(i).widget
        layout.removeWidget(widget_to_remove)
        widget_to_remove.deleteLater()


def init_lucidity_templates(current_project_p, current_type_p):
    # Init lucidity templates
    root = str(Path(conf.pipeline_path) / current_project_p).replace(os.sep, "/")

    templates = []

    templates_array = conf.lucidity_templates.get(current_type_p)

    for tmpl_part in templates_array:
        arg = [root, templates_array.get(tmpl_part)]
        tmpl_arg = '/'.join(arg)

        tmpl = lucidity.Template(tmpl_part,
                                 tmpl_arg,
                                 anchor=lucidity.Template.ANCHOR_END)

        templates.append(tmpl)

    conf.templates = templates
    pprint(conf.templates)


if __name__ == "__main__":
    init_lucidity_templates('MMOVIE', 'assets')