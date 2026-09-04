# puts src/ on sys.path so the modules under test import without installing the project

import sys
from pathlib import Path

src_directory = Path(__file__).resolve().parent.parent / "src"
if str(src_directory) not in sys.path:
    sys.path.insert(0, str(src_directory))

# and experiments/ beside it, so e1's script is importable by its own tests. it is
# a script and not a package, and the tests exercise its pure parts directly.
experiments_directory = Path(__file__).resolve().parent.parent / "experiments"
if str(experiments_directory) not in sys.path:
    sys.path.insert(0, str(experiments_directory))
