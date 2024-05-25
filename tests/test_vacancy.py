import pytest
from src.vacancy import Vacancy


def test_vacancy_init():
    vacancy = Vacancy('title', 'url', 1000, 'full-time')
    assert vacancy.title == 'title'
    assert vacancy.url == 'url'
    assert vacancy.salary == 1000
    assert vacancy.schedule == 'full-time'

