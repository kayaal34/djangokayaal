from django.contrib import admin

from .models import *


class SalaryPerYearGraphicsAdmin(admin.ModelAdmin):
    list_display = ("title", "photo")
    list_display_links = ("title", "photo")
    search_fields = ("title",)


class VacanciesPerCityGraphicsAdmin(admin.ModelAdmin):
    list_display = ("title", "photo")
    list_display_links = ("title", "photo")
    search_fields = ("title",)


class SalaryAndVacanciesPerYearsProfessionTableAdmin(admin.ModelAdmin):
    list_display = ("year", "average_salary", "average_salary_profession", "vacancies_count",
                    "vacancies_count_profession")
    list_display_links = ("year", "average_salary", "average_salary_profession", "vacancies_count",
                          "vacancies_count_profession")
    search_fields = ("year",)


class SalaryPerCityTableAdmin(admin.ModelAdmin):
    list_display = ("city", "salary")
    list_display_links = ("city", "salary")
    search_fields = ("year",)


class VacanciesPerCityTableAdmin(admin.ModelAdmin):
    list_display = ("city", "vacancy_rate")
    list_display_links = ("city", "vacancy_rate")
    search_fields = ("year",)


class SkillPerYearsAdmin(admin.ModelAdmin):
    list_display = ("year", "first_vacancy", "second_vacancy", "third_vacancy", "fourth_vacancy", "fifth_vacancy",
                    "sixth_vacancy", "seventh_vacancy", "eighth_vacancy", "ninth_vacancy", "tenth_vacancy")
    list_display_links = ("year", "first_vacancy", "second_vacancy", "third_vacancy", "fourth_vacancy", "fifth_vacancy",
                          "sixth_vacancy", "seventh_vacancy", "eighth_vacancy", "ninth_vacancy", "tenth_vacancy")
    search_fields = ("year", "first_vacancy", "second_vacancy", "third_vacancy", "fourth_vacancy", "fifth_vacancy",
                     "sixth_vacancy", "seventh_vacancy", "eighth_vacancy", "ninth_vacancy", "tenth_vacancy")


admin.site.register(SalaryPerYearsGraphics, SalaryPerYearGraphicsAdmin)
admin.site.register(VacanciesPerCityGraphics, VacanciesPerCityGraphicsAdmin)
admin.site.register(SalaryAndVacanciesPerYearsProfessionTable, SalaryAndVacanciesPerYearsProfessionTableAdmin)
admin.site.register(SalaryPerCityTable, SalaryPerCityTableAdmin)
admin.site.register(VacanciesPerCityTable, VacanciesPerCityTableAdmin)
admin.site.register(SkillsPerYears, SkillPerYearsAdmin)
