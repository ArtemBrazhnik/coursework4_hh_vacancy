class Vacancy:
    """Информация о вакансии"""

    title: str
    url: str
    salary: int
    schedule: str

    def __init__(self, title, url, salary, schedule):
        self.title = title
        self.url = url
        self.salary = salary or 0
        self.schedule = schedule

    def __str__(self):
        return f'{self.title} {self.salary} {self.schedule} {self.url}'

    def __gt__(self, other):
        return self.salary > other.salary

    def to_json(self) -> dict:
        """Конвертирует вакансии в JSON"""
        return {
            'title': self.title,
            'url': self.url,
            'salary': self.salary,
            'schedule': self.schedule,
        }
