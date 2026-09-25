import os
import sys
from pathlib import Path

import gnr

GNR_TESTS = Path(gnr.__file__).resolve().parents[1] / 'tests'
sys.path.insert(0, str(GNR_TESTS))
os.environ.setdefault('GNR_LOCAL_PROJECTS', str(Path(__file__).resolve().parents[2]))
