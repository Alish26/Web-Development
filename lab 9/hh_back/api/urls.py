from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('companies/', show_companies),
    path('companies/<int:company_id>/', show_company),
    path('companies/<int:company_id>/vacancies/', show_company_vacancies),
    path('vacancies/', show_vacancies),
    path('vacancies/<int:vacancy_id>/', show_vacancy),
    path('vacancies/top-ten/', show_top_ten_vacancies)
]
