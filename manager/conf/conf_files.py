from pathlib import Path
from manager.p import private_conf

import os
import lucidity

# v Parameters ==================================================
# Entity part layout
altRowColors = True

# ^ Parameters ==================================================
# v Credentials =================================================
# School shotgun
sg_link = private_conf.sg_link
sg_login = private_conf.sg_login
sg_key = private_conf.sg_key

# ^ Credentials =================================================
# v Dictionaries ================================================
references = {
    'assets': 'assets',
    'shots': 'shots'
}

# Shotgrid
sg_translation = {
    references.get('assets'): 'Asset',
    'category': ['sg_asset_type', 'is'],
    'name': ['code', 'is'],
    'task': ['step', 'is'],

    references.get('shots'): 'Shot',
    'sqNb': ['code', 'starts_with'],
    'shNb': ['code', 'ends_with']
}

# ^ Dictionaries ================================================
# v Projects and types ==========================================
projects = {
    "<Project>": {
        "name": "Placeholder",
        "sg_id": None
    },
    "micromovie": {
        "name": "MMOVIE",
        "sg_id": 1095
    }
}

types = ["<Type>", references.get('assets'), references.get('shots')]

table_labels = {
    references.get('assets'): ["Category", "Name", "Task", "Vers. nb", "State"],
    references.get('shots'): ["Sequence nb", "Shot nb", "Task", "Vers. nb", "State"]
}
tables_order = {
    'assets': ['type', 'category', 'name', 'task', 'versionNb', 'state', 'ext'],
    'shots': ['type', 'sqNb', 'shNb', 'task', 'versionNb', 'state', 'ext']
}
labels_to_lu_templates = {
    'Project': 'project',
    'Type': 'type',
    'Category': 'category',
    'Name': 'name',
    'Task': 'task',
    'Vers. nb': 'versionNb',
    'State': 'state',
    'File name': 'ext',

    'Sequence nb': 'sqNb',
    'Shot nb': 'shNb'
}

# ^ Projects and types ==========================================
# v Software and extensions =====================================
software_list = {
    "Maya": ["ma", "mb"],
    "Houdini": ["hipnc"],
    "Nuke": ["nk"]
}

# ^ Software and extensions =====================================
# v Paths =======================================================
# Turn point ===========================
use_fs = ["category", "sqNb"]

# Classic paths ========================
ui_path = Path(__file__).parent.parent / "ui" / "qt" / "window.ui"
project_root = Path('D:/TD4/Paul/Pipeline')

shot_file_pattern = 'shots/sq*/sh*/*/v*/sh*_*.{ext}'
shot_file_split_pattern = {
    'shots',
    'sq*',

}
asset_file_pattern = 'assets/*/*/*/v*/*.{ext}'

general_file_pattern = '{type}/*/*/{task}/v*/*_{state}.{ext}'

# Lucidity =============================
default_project = "micromovie"
current_project_name = projects.get(default_project).get("name")

root = lucidity.Template('root', str(Path(project_root) / current_project_name).replace(os.sep, "/"))  # todo
resolver = {root.name: root}

assets_template = lucidity.Template('asset',
                                    '{@root}/{type}/{category}/{name}/{task}/v{versionNb}/{name}_{state}.{ext}',
                                    template_resolver=resolver)  # , anchor=lucidity.Template.ANCHOR_END
shots_template = lucidity.Template('shot',
                                   '{@root}/{type}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state}.{ext}',
                                   template_resolver=resolver)  # , anchor=lucidity.Template.ANCHOR_END
general_template = lucidity.Template('general',
                                     '{@root}/{type}',
                                     template_resolver=resolver)

templates = [shots_template, assets_template, general_template]

lucidity_templates = {
    'assets': {
        'ext': r'{type:assets}/{category}/{name}/{task}/{versionNb:(v\d\d\d)}/{name}_{state:(publish|work)}.{ext}',
        'state': r'{type:assets}/{category}/{name}/{task}/{versionNb:(v\d\d\d)}/{name}_{state:(publish|work)}',
        'versionNb': r'{type:assets}/{category}/{name}/{task}/{versionNb:(v\d\d\d)}',
        'task': '{type:assets}/{category}/{name}/{task:(modeling|rigging|surfacing)}',
        'name': '{type:assets}/{category}/{name}',
        'category': '{type:assets}/{category}',
        'type': '{type:assets}'
    },
    'shots': {
        'ext': r'{type:shots}/{sqNb:(sq\d\d\d)}/{shNb:(sh\d\d\d)}/{task}/{versionNb:(v\d\d\d)}/{shNb:(sh\d\d\d)}_{state:(publish|work)}.{ext}',
        'state': r'{type:shots}/{sqNb:(sq\d\d\d)}/{shNb:(sh\d\d\d)}/{task}/{versionNb:(v\d\d\d)}/{shNb:(sh\d\d\d)}_{state:(publish|work)}',
        'versionNb': r'{type:shots}/{sqNb:(sq\d\d\d)}/{shNb:(sh\d\d\d)}/{task}/{versionNb:(v\d\d\d)}',
        'task': r'{type:shots}/{sqNb:(sq\d\d\d)}/{shNb:(sh\d\d\d)}/{task}',
        'shNb': r'{type:shots}/{sqNb:(sq\d\d\d)}/{shNb:(sh\d\d\d)}',
        'sqNb': r'{type:shots}/{sqNb:(sq\d\d\d)}',
        'type': '{type:shots}'
    }
}

# ^ Paths =======================================================
