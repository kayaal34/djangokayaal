from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('востребованность/', demand, name="demand"),
    path('география/', geography, name="geography"),
    path('навыки/', skills, name="skills"),
    path('вакансии/', vacancy, name="vacancy")
]

