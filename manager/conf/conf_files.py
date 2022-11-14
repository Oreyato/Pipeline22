from pathlib import Path

import os
import lucidity

# v Credentials =================================================
# School shotgun
sg_link = "https://artfx.shotgunstudio.com"
sg_login = "test_td"
sg_key = "uqtcaegzgsqzDf6ttkz%lkgfw"

# ^ Credentials =================================================
# v Projects and types ==========================================
projects = {
    "<Project>": "Placeholder",
    "micromovie": "MMOVIE",
    "td_test": {
        "sg_name": "TD4_Pipeline_Workshop_project_2022",
        "sg_id": 1095
    }
}

types = ["<Type>", "assets", "shots"]

table_labels = {
    "assets": ["Category", "Name", "Task", "Vers. nb", "State", "File name"],
    "shots": ["Sequence nb", "Shot nb", "Task", "Vers. nb", "State", "File name"]
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
# Classic paths ========================
ui_path = Path(__file__).parent.parent / "ui" / "qt" / "window.ui"
pipeline_path = Path('D:/TD4/Paul/Pipeline')

shot_file_pattern = 'shots/sq*/sh*/*/v*/sh*_*.{ext}'
asset_file_pattern = 'assets/*/*/*/v*/*.{ext}'

general_file_pattern = '{type}/*/*/{task}/v*/*_{state}.{ext}'

# Lucidity =============================
root = lucidity.Template('root', str(Path(pipeline_path) / projects.get("micromovie")).replace(os.sep, "/"))
resolver = {root.name: root}

assets_template = lucidity.Template('asset',
                                    '{@root}/{type}/{category}/{name}/{task}/v{versionNb}/{name}_{state}.{ext}',
                                    template_resolver=resolver, anchor=lucidity.Template.ANCHOR_END)
shots_template = lucidity.Template('shot',
                                   '{@root}/{type}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state}.{ext}',
                                   template_resolver=resolver, anchor=lucidity.Template.ANCHOR_END)
general_template = lucidity.Template('general',
                                     '{@root}/{type}',
                                     template_resolver=resolver)

templates = [shots_template, assets_template, general_template]

# ^ Paths =======================================================