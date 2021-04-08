from re import L
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i * 1000
    }
    for i in range(1, 11)
]

def list_products(request):
    
    return JsonResponse(products, safe=False)


def show_product(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)

    return JsonResponse({'message': 'Product doesn\'t exist '})

categories = [
    {
        'id': i,
        'name': f'Category {i}'
    }
    for i in range(1, 11)
]

def list_categories(request):

    return JsonResponse(categories, safe=False)

def show_category(request, category_id):
    for category in categories:
        if category['id'] == category_id:
            return JsonResponse(category)

    return JsonResponse({'message': 'Category doesn\'t exist '})