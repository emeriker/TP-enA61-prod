import os
file_path = str(os.getcwd()) + '/../VERSION'
print(file_path)
with open(file_path) as file:
    api_version = file.read().replace('\n', '')


print(api_version)
