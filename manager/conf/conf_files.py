from pathlib import Path

# v Credentials =================================================
# School shotgun
sg_link = "https://artfx.shotgunstudio.com"
sg_login = "test_td"
sg_key = "uqtcaegzgsqzDf6ttkz%lkgfw"

# ^ Credentials =================================================
# v Paths =======================================================
ui_path = Path(__file__).parent.parent / "ui" / "qt" / "window.ui"
pipeline_path = Path('D:/TD4/Paul/Pipeline')

shot_file_pattern = 'shots/sq*/sh*/*/v*/sh*_*.{ext}'
asset_file_pattern = 'assets/*/*/*/v*/*.{ext}'

general_file_pattern = '{type}/*/*/{task}/v*/*_{state}.{ext}'

# ^ Paths =======================================================
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
