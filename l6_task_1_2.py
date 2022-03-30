# -----------------------------------------------------1--2-------------------------------------------------------------
# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

remote_addr = []
result = []

with open('nginx_logs.txt', 'r') as f:
    for line in f:
        remote_ad = line.split(' ')[0]
        remote_addr.append(remote_ad)
        request_type = line.split('"')[1].split(' ')[0]
        requested_resource = line.split('"')[1].split(' ')[1]
        t = (remote_ad, request_type, requested_resource)
        result.append(t)

print(result)
# ----------------------------------------------------2-----------------------------------------------------------------
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

r_addr_dict = {}
for ip in remote_addr:
    if ip not in r_addr_dict:
        r_addr_dict[ip] = 1
    else:
        r_addr_dict[ip] += 1

for k, v in r_addr_dict.items():
    if v == max(r_addr_dict.values()):
        print(f'spammer is {k}')
        print(f'request count: {v}')
