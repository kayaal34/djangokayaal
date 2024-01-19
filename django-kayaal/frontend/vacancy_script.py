import requests
import json


def get_data(day):
    needed_vacancies = ['frontend', 'фронтенд', 'вёрстка', 'верстка', 'верста', 'front end', 'angular', 'html',
                        'css', 'react', 'vue']
    info = {'name': [], "salary": [],
            'area_name': [], 'published_at': [], "employer_name": [],
            "snippet_requirement": [], "snippet_responsibility": [], }
    published_at_list = []
    next_day = day + 1
    if next_day < 10:
        next_day = f"0{next_day}"
    if day < 10:
        day = f"0{day}"
    for date_from in [f'2022-12-{day}T00:00:00', f'2022-12-{day}T06:00:00', f'2022-12-{day}T12:00:00', f'2022-12-{day}T18:00:00',
                      f'2022-12-{next_day}T00:00:00']:
        date_to = f'2022-12-{next_day}T00:00:00'
        if len(published_at_list) >= 10:
            break
        for page in range(1, 20):
            request = requests.get(
                f'https://api.hh.ru/vacancies?date_from={date_from}&date_to={date_to}&specialization=1&per_page=100&page={page}')
            for item in json.loads(request.text)['items']:
                is_correct = False
                vacancy = list(map(lambda x: x.lower(), item['name'].split()))
                for element in vacancy:
                    if element in needed_vacancies:
                        is_correct = True
                flag = False
                if not is_correct:
                    continue
                for element in published_at_list:
                    if element == item["published_at"]:
                        flag = True
                if not flag and len(published_at_list) < 10:
                    published_at_list.append(item["published_at"])
                    info['name'].append(item['name'])
                    salary = item['salary']
                    salary_from, salary_to, salary_currency = None, None, None

                    if salary is not None:
                        salary_from = salary['from']
                        salary_to = salary['to']
                        salary_currency = salary['currency']
                    salary_currency = "" if salary_currency is None else " " + salary_currency
                    if salary_from is None:
                        info["salary"].append(str(salary_to) + salary_currency)
                    elif salary_to is None:
                        info["salary"].append(str(salary_from) + salary_currency)
                    else:
                        info["salary"].append(str(((salary_from + salary_to) / 2)) + salary_currency)

                    snippet = item['snippet']
                    employer = item['employer']
                    info["snippet_requirement"].append(snippet['requirement'])
                    info["snippet_responsibility"].append(snippet['responsibility'])
                    info["employer_name"].append(employer["name"])
                    area = item['area']
                    area_name = None
                    if area is not None:
                        area_name = area['name']
                    info['area_name'].append(area_name)
                    info['published_at'].append(item['published_at'])
    return info
