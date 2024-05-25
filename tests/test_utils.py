import pytest
from src.utils import get_vacancies_by_salary


def test_get_vacancies_by_salary():
    vacancies = [
        {'title': 'title1', 'salary': 1000},
        {'title': 'title2', 'salary': 2000},
        {'title': 'title3', 'salary': 3000},
        {'title': 'title4', 'salary': 10000},
        {'title': 'title5', 'salary': 5000},
        {'title': 'title6', 'salary': 6000},
        {'title': 'title7', 'salary': 8000},
        {'title': 'title8', 'salary': 7000},
        {'title': 'title9', 'salary': 9000},
        {'title': 'title10', 'salary': 4000},
        {'title': 'title11', 'salary': 11000},
        ]
    salary_range = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]
