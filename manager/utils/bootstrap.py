import sys
from pathlib import Path

here = Path(__file__)
root = here.parent.parent.parent

packages = root / "venv" / "Lib" / "site-packages"
print(root)
print(packages)

sys.path.append(str(packages))