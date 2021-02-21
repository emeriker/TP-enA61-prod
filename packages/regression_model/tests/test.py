import pathlib
absoPath = str(pathlib.Path().absolute()) + '/..'
print(absoPath)

import sys
sys.path.append(absoPath)

from regression_model.predict import make_prediction
