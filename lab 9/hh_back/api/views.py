from re import L
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *

def show_companies(request):
    companies = Company.objects.all()
    companies = [company.to_json() for company in companies]
    return JsonResponse(companies, safe=False)

def show_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExit as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(company.to_json())

def show_company_vacancies(request, company_id):
        vacancies = Vacancies.objects.all()
        result = []
        for vacancy in vacancies:
            if vacancy.company.id == company_id:
                result.append(vacancy.to_json())

        return JsonResponse(result, safe=False)

def show_vacancies(request):
    vacancies = Vacancies.objects.all()
    vacancies = [vacancy.to_json() for vacancy in vacancies]

    return JsonResponse(vacancies, safe=False)

def show_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancies.objects.get(id=vacancy_id)
    except Vacancies.DoesNotExit as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

def show_top_ten_vacancies(request):
    vacancies = Vacancies.objects.all()
    vacancies = [vacancy.to_json() for vacancy in vacancies][:10]

    return JsonResponse(vacancies, safe=False)