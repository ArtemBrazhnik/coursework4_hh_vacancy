import json
import os
from src.api import HHApi


class JSONSaver:
    def dump_to_file(self, vacancies, filename="vacancies.json", directory="data"):
        full_path = os.path.join(directory, filename)
        vacancies_data = [vacancy.to_json() for vacancy in vacancies]
        with open(full_path, 'w', encoding='UTF-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False, indent=4)
        print(f"Данные успешно сохранены в {full_path}")
