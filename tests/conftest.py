# puts src/ on sys.path so the modules under test import without installing the project

import sys
from pathlib import Path

src_directory = Path(__file__).resolve().parent.parent / "src"
if str(src_directory) not in sys.path:
    sys.path.insert(0, str(src_directory))
