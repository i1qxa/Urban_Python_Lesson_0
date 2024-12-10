import os
from datetime import datetime

directory = os.getcwd()
for i in os.walk("."):
    for j in i[2]:
        file_path = os.path.abspath(j)
        file_change_time = datetime.fromtimestamp(os.path.getmtime(j)).strftime("%H:%M:%S")
        file_size = os.path.getsize(j)
        dir_name = os.path.dirname(file_path)
        print(
            f"{file_path} Время последнего изменения: {file_change_time} Размер файла: {file_size}б Название папки: {dir_name}")
