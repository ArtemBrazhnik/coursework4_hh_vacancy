import requests
from src.vacancy import Vacancy
from abc import ABC, abstractmethod


class GetVacancies(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HHApi(GetVacancies):
    """получение вакансий с API HH.ru"""

    def __init__(self):
        self.URL = 'https://api.hh.ru/'

    def get_vacancies(self, title):
        params = {
            'text': title,
            'area': 1,
            'per_page': 100
        }
        response = requests.get(url=f'{self.URL}vacancies', params=params)

        vacancies = []
        for item in response.json()['items']:
            vacancies.append(
                Vacancy(
                    title=item.get('name'),
                    url=item.get('alternate_url'),
                    salary=(item.get('salary') or {}).get('to', 0),
                    schedule=item.get('schedule').get('name')
            )
            )
        return vacancies
