from pathlib import Path

import os
import lucidity

# v Credentials =================================================
# School shotgun
sg_link = "https://artfx.shotgunstudio.com"
sg_login = "test_td"
sg_key = "uqtcaegzgsqzDf6ttkz%lkgfw"

# ^ Credentials =================================================
# v Dictionaries ================================================
references = {
    'assets': 'assets',
    'shots': 'shots'
}

# Shotgrid
sg_translation = {
    references.get('assets'): 'Asset',
    references.get('shots'): 'Shot'
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
    references.get('assets'): ["Category", "Name", "Task", "Vers. nb", "State", "File name"],
    references.get('shots'): ["Sequence nb", "Shot nb", "Task", "Vers. nb", "State", "File name"]
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
software_programs = {
    "Maya": ["ma", "mb"],
    "Houdini": ["hipnc"],
    "Nuke": ["nk"],
    "Photoshop": ["psd"],
    "AfterEffects": ["ae"]
}

# ^ Software and extensions =====================================
# v Paths =======================================================
# Turn point ===========================
turn_point = "versionNb"

# Classic paths ========================
ui_path = Path(__file__).parent.parent / "ui" / "qt" / "window.ui"
pipeline_path = Path('D:/TD4/Paul/Pipeline')
# pipeline_path = Path('F:/Cours/Y004/Prog/Pipeline')

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

root = lucidity.Template('root', str(Path(pipeline_path) / current_project_name).replace(os.sep, "/"))  # todo
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
        'ext': '{type:shots}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state=(publish|work)}.{ext}',
        'state': '{type:shots}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state=(publish|work)}',
        'versionNb': '{type:shots}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}',
        'task': '{type:shots}/sq{sqNb}/sh{shNb}/{task}',
        'shNb': '{type:shots}/sq{sqNb}/sh{shNb}',
        'sqNb': '{type:shots}/sq{sqNb}',
        'type': '{type:shots}'
    }
}

# ^ Paths =======================================================
