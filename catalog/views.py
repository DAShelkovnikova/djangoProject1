

from django.shortcuts import render


from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'base.html', context)

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')






# Create your views here.
