# -----------------------------------------------------5----------------------------------------------------------------
# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import os
import json


given_folder = 'virt'
files = []
out_dict = {}
for root, dirname, filenames in os.walk(given_folder):
    for file in filenames:
        file_path = os.path.join(root, file)
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        files.append((ext, os.stat(file_path).st_size))
# print(files)
# print(type(files))
max_size = max(files, key=lambda x: x[1])[1]

# print(max_size)
i = 1
for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = (0, [])

for file in files:
    num, ext_list = out_dict[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    out_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)

print(out_dict)

with open(os.path.basename(os.getcwd()) + 'summary.json', 'a', encoding='utf-8') as json_file:
    json.dump(out_dict,json_file)
