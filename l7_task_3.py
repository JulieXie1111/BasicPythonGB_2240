# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
# решена, например, во фреймворке django.

import os
import shutil

my_dir = 'templates'  # save folder
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'  # search folder
files = []

for root, dirs, filenames in os.walk(folder):
    # print(f'root: {root}')
    # print(f'dirs: {dirs}')
    # print(filenames)
    for file in filenames:
        if '.html' in file:
            files.append(os.path.join(root, file))

# print(files)

for path in files:
    # print(f"path: {path}")
    # print(f'dirname: {os.path.dirname(path)}')
    # print(f'{os.path.basename(os.path.dirname(path))}')
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    # print(f'folder: {folder}')
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    # print(f'save path: {save_path}')

    shutil.copy(path, save_path)

