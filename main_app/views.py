from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import SkincareProduct


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def morning(request):
    skincare_products = SkincareProduct.objects.all()
    # for product in skincare_products:
    #     product.image_url = f"{product.image}"

    return render(request, 'skincare/morning.html', {'skincare_products': skincare_products})

# def sk_product_detail(request):
#     skincare_product = SkincareProduct.objects.get(id=skincare_product_id)
#     return render(request, 'skincare/product.html', {'skincare_product': skincare_product})