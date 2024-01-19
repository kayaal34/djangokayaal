from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from .forms import *
from .vacancy_script import *


def index(request):
    return render(request, 'frontend/index.html', {'title': "Frontend"})


def demand(request):
    demand_table_info = SalaryAndVacanciesPerYearsProfessionTable.objects.all()
    demand_graphic_info = SalaryPerYearsGraphics.objects.all()
    context = {
        'title': "Востребованность",
        "demand_table_info": demand_table_info,
        "demand_graphic_info": demand_graphic_info
    }
    return render(request, 'frontend/demand.html', context=context)


def geography(request):
    geography_vacancies_table_info = VacanciesPerCityTable.objects.all()
    geography_graphic_info = VacanciesPerCityGraphics.objects.all()
    geography_salary_table_info = SalaryPerCityTable.objects.all()
    context = {
        'title': "География",
        "geography_vacancies_table_info": geography_vacancies_table_info,
        "geography_graphic_info": geography_graphic_info,
        "geography_salary_table_info": geography_salary_table_info
    }
    return render(request, 'frontend/geography.html', context=context)


def skills(request):
    skills_data = SkillsPerYears.objects.all()
    context = {
        'title': "Навыки",
        "skills_data": skills_data
    }
    return render(request, 'frontend/skills.html', context=context)


def vacancy(request):
    data = [{'name': "", "salary": "",
            'area_name': "", 'published_at': "", "employer_name": "",
            "snippet_requirement": "", "snippet_responsibility": "", }]
    flag = False
    new_date = []
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            data = get_data(int(form.cleaned_data['day']))
            flag = len(data["name"]) != 0
            for i in range(len(data['name'])):
                new_date.append({'name': data['name'][i], "salary": "Не указано" if data['salary'][i] == "None" else data['salary'][i],
            'area_name':  "Не указано" if data['area_name'][i] == "None" else data['area_name'][i], 'published_at': data['published_at'][i][:10] + " " + data['published_at'][i][11:19], "employer_name": data['employer_name'][i],
            "snippet_requirement": "Не указано" if data['snippet_requirement'][i] == "None" else data['snippet_requirement'][i], "snippet_responsibility": "Не указано" if data["snippet_responsibility"][i] == "None" else data["snippet_responsibility"][i]})
            new_date.sort(key= lambda vacancy: vacancy["published_at"])
    else:
        form = AddForm()
    context = {
        'title': "Последние вакансии",
        'form': form,
        'data': new_date,
        'flag': flag,
    }
    return render(request, 'frontend/vacancy.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
