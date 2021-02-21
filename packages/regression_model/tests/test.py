import pathlib
absoPath = str(pathlib.Path().absolute()) + '/..'
print(absoPath)

import sys
sys.path.append(absoPath)
print('----------------------')
print(sys.path)



from ml_api.api import __version__ as api_version
from regression_model.predict import make_prediction


