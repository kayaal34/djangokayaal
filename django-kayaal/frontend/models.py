from django.db import models


class SalaryPerYearsGraphics(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photo", verbose_name="Фото")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Заработная плата - графики"
        verbose_name_plural = "Заработная плата - графики"


class VacanciesPerCityGraphics(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photo", verbose_name="Фото")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Количество вакансий по городам - графики"
        verbose_name_plural = "Количество вакансий по городам - графики"


class SalaryAndVacanciesPerYearsProfessionTable(models.Model):
    year = models.IntegerField(verbose_name="год")
    average_salary = models.IntegerField(verbose_name="средняя заработная плата")
    average_salary_profession = models.IntegerField(verbose_name="средняя заработная плата-frontend")
    vacancies_count = models.IntegerField(verbose_name="количество вакансий")
    vacancies_count_profession = models.IntegerField(verbose_name="количество вакансий-frontend")

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Количество вакансий и зарплата по годам по профессии frontend - табличные данные"
        verbose_name_plural = "Количество вакансий и зарплата по годам по профессии frontend - табличные данные"


class SalaryPerCityTable(models.Model):
    city = models.CharField(max_length=255, verbose_name="город")
    salary = models.IntegerField(verbose_name="зарплата")

    def __str__(self):
        return str(self.city) + "-" + str(self.salary)

    class Meta:
        verbose_name = "Зарплата по городам - табличные значения"
        verbose_name_plural = "Зарпалата по городам - табличные значения"


class VacanciesPerCityTable(models.Model):
    city = models.CharField(max_length=255, verbose_name="город")
    vacancy_rate = models.FloatField(verbose_name="количество вакансий")

    def __str__(self):
        return str(self.city) + "-" + str(self.vacancy_rate)

    class Meta:
        verbose_name = "Количество вакансий по городам - табличные значения"
        verbose_name_plural = "Количество вакансий по городам - табличные значения"


class SkillsPerYears(models.Model):
    year = models.IntegerField(verbose_name="год")
    first_vacancy = models.CharField(max_length=255, verbose_name="первый навык")
    second_vacancy = models.CharField(max_length=255, verbose_name="второй навык")
    third_vacancy = models.CharField(max_length=255, verbose_name="третий навык")
    fourth_vacancy = models.CharField(max_length=255, verbose_name="четвертый навык")
    fifth_vacancy = models.CharField(max_length=255, verbose_name="пятый навык")
    sixth_vacancy = models.CharField(max_length=255, verbose_name="шестой навык")
    seventh_vacancy = models.CharField(max_length=255, verbose_name="седьмой навык")
    eighth_vacancy = models.CharField(max_length=255, verbose_name="восьмой навык")
    ninth_vacancy = models.CharField(max_length=255, verbose_name="девятый навык")
    tenth_vacancy = models.CharField(max_length=255, verbose_name="десятый навык")
    photo = models.ImageField(upload_to="photo", verbose_name="Фото", null=True)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"
