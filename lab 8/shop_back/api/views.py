from re import L
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category

# Create your views here.
def list_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def show_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExit as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(product.to_json())


def list_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def show_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExit as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(category.to_json())