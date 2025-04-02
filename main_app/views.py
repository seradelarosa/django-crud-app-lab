from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SkincareProduct


# Define the home view function
def home(request):
    return render(request, 'home.html')

def all_skincare(request):
    skincare_products = SkincareProduct.objects.all()
    return render(request, 'skincare/all_skincare.html', {'skincare_products': skincare_products})

def morning(request):
    skincare_products = SkincareProduct.objects.all()
    # for product in skincare_products:
    #     product.image_url = f"{product.image}"
    return render(request, 'skincare/morning.html', {'skincare_products': skincare_products})

def evening(request):
    skincare_products = SkincareProduct.objects.all()
    return render(request, 'skincare/evening.html', {'skincare_products': skincare_products})

def weekly(request):
    skincare_products = SkincareProduct.objects.all()
    return render(request, 'skincare/weekly.html', {'skincare_products': skincare_products})

def product_detail(request, product_id):
    skincare_product = SkincareProduct.objects.get(id=product_id)
    return render(request, 'skincare/product_detail.html', {'product': skincare_product})

class ProductCreate(CreateView):
    model = SkincareProduct
    fields = '__all__'

class ProductUpdate(UpdateView):
    model = SkincareProduct
    fields = '__all__'

class ProductDelete(DeleteView):
    model = SkincareProduct
    success_url = '/skincare/all_skincare/'