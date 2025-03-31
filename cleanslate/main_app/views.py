from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .fixtures.skincare_data import skincare_products


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def morning(request):
    # for product in skincare_products:
    #     product.image_url = f"{product.image}"

    return render(request, 'skincare/morning.html', {'skincare_products': skincare_products})

# def my_view(request):
#     context = {
#         'class_a': class_a_instances,
#         'class_b': class_b_instances,
#         'class_c': class_c_instances,
#     }
#     return render(request, 'myapp/template.html', context)