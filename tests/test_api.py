import pytest
from src.api import HHApi


def test_hh_api_init():
    hh_api = HHApi()
    assert hh_api.URL == 'https://api.hh.ru/'
    