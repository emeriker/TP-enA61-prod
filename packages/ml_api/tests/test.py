
import pathlib
absoPathVersion = str(pathlib.Path().absolute()) + '/../VERSION'
absoPath = str(pathlib.Path().absolute()) + '/../api'

import sys
sys.path.append(absoPath)

api_version = ''
with open(absoPathVersion) as file:
    api_version = file.read().replace('\n', '')
print(api_version)

from app import create_app