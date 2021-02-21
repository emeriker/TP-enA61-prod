import os
absoPath = ''
for folder in str(os.path.realpath(__file__)).split('/')[:-1]:
    absoPath += folder + '/'
absoPath += 'api/'
import sys
print(absoPath)
sys.path.append(absoPath)

from app import create_app
from config import DevelopmentConfig


application = create_app(
    config_object=DevelopmentConfig)


if __name__ == '__main__':
    application.run()
