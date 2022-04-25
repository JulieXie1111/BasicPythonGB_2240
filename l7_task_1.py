"""Task_1"""
# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
# конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

my_dir = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']
for f in folders:
    dir_path = os.path.join(my_dir, f)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(my_dir, 'exists')

# ----------------------------------------------------------------------------------------------------------------------

# pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
# for root, folders in pattern.items():
#     if os.path.exists(root):
#         print(root, 'exists')
#     else:
#         for folder in folders:
#             curr_dir = os.path.join(root, folder)
#             if not os.path.exists(curr_dir):
#                 os.makedirs(curr_dir)
