from src.api import HHApi
from src.jsonsaver import JSONSaver

hh = HHApi()
json_saver = JSONSaver()


def get_vacancies_by_salary(vacancies, salary_range):
    """Фильтр по зарплате"""
    filtered_by_salary = []

    for vacancy in vacancies:
        if vacancy.salary in salary_range:
            filtered_by_salary.append(vacancy)

    return filtered_by_salary


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)


def user_interaction():
    """Взаимодействие с пользователем для поиска вакансий"""

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range = list(map(int, input("Введите диапазон зарплат: ").split()))

    vacancies_list = hh.get_vacancies(search_query)

    ranged_vacancies = get_vacancies_by_salary(vacancies_list, salary_range)

    sorted_vacancies = sorted(ranged_vacancies, key=lambda x: x.salary, reverse=True)
    top_vacancies = sorted_vacancies[:top_n]

    print_vacancies(top_vacancies)

    json_saver.dump_to_file(top_vacancies)
