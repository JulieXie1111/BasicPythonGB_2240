# --------------------------------------------------------2-------------------------------------------------------------
"""Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt"""
import re
import requests

RE_PARSER = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                       r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                       r'([/\w+]{0,}) (?:[^\"]*)." ([0-9]+) ([0-9]+)')
url = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"

for stuff in RE_PARSER.findall(requests.get(url).text):
    remote_addr, request_datetime, request_type, requested_resource, response_code, response_size = stuff
    print(remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
