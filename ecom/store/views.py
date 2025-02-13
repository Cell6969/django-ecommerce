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
def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product' : product}
    return render(request, 'store/product-info.html', context=context)