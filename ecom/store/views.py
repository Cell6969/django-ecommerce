from django.shortcuts import render
from django.views.decorators.http import require_GET
from . models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.

@require_GET
def store(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'store/store.html', context=context)

def categories(request):
    categories_all = Category.objects.all()
    return {"categories": categories_all} 

@require_GET
def list_category(request,category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    context = {
        'category' : category,
        'products': products
    }

    return render(request, 'store/list-category.html', context=context)

@require_GET
def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product' : product}
    return render(request, 'store/product-info.html', context=context)