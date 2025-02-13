from django.shortcuts import render
from django.views.decorators.http import require_GET
from . models import Category, Product

# Create your views here.

@require_GET
def store(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'store/store.html', context=context)

def categories(request):
    categories_all = Category.objects.all()
    return {"categories": categories_all} 