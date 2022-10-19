from pathlib import Path

# v Paths =======================================================
ui_path = Path(__file__).parent.parent / "ui" / "qt" / "window.ui"
pipeline_path = Path('D:/TD4/Paul/Pipeline')

shot_file_pattern = 'shots/sq*/sh*/*/v*/sh*_*.{ext}'
asset_file_pattern = 'assets/*/*/modeling/v*/*.{ext}'

general_file_pattern = '{type}/*/*/{task}/v*/*_{state}.{ext}'

# ^ Paths =======================================================
# v Projects ====================================================
projects = {
    "micromovie": "MMOVIE"
}

# ^ Projects ====================================================
# v Software and extensions =====================================
software_programs = {
    "Maya": ["ma", "mb"],
    "Houdini": ["hipnc"],
    "Nuke": ["nk"],
    "Photoshop": ["psd"]
}

# ^ Software and extensions =====================================
