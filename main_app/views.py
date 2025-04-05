from django.shortcuts import render, get_object_or_404, redirect
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import SkincareProduct, UsageLog


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
    # Fetch the product using the ID
    skincare_product = get_object_or_404(SkincareProduct, id=product_id)
    
    # Fetch usage logs for this specific product
    usage_logs = UsageLog.objects.filter(product=skincare_product).order_by('-usage_time')

    if request.method == 'POST':
        # Get the data from the form
        usage_category = request.POST.get('usage_category')
        usage_date = request.POST.get('usage_date')
        usage_time = request.POST.get('usage_time')

        # Combine date and time into a single datetime object
        usage_datetime = timezone.make_aware(
            timezone.datetime.strptime(f"{usage_date} {usage_time}", "%Y-%m-%d %H:%M")
        )

        # Create the new usage log for the selected product
        UsageLog.objects.create(
            product=skincare_product,
            usage_category=usage_category,
            usage_time=usage_datetime,
        )

        # Redirect to the same page to see the updated logs
        return redirect('product_detail', product_id=product_id)

    # If it's a GET request, just display the page
    return render(request, 'skincare/product_detail.html', {
        'product': skincare_product,
        'usage_logs': usage_logs,
    })


def usage_logs(request):
    # Get all usage logs, ordered by most recent
    usage_logs = UsageLog.objects.all().order_by('-usage_time')

    # Get the current date and find the start of the current week (Monday)
    start_of_week = timezone.now() - timezone.timedelta(days=timezone.now().weekday())

    # Create a list of days of the week (0 to 6) starting from Monday
    days_of_week = [start_of_week + timezone.timedelta(days=i) for i in range(7)]

        # Fetch all skincare products to display in the form
    skincare_products = SkincareProduct.objects.all()

    # Pass data to the template
    context = {
        'usage_logs': usage_logs,
        'days_of_week': days_of_week,
        'skincare_products': skincare_products,
    }

    return render(request, 'logs/usage_logs.html', context)

def add_usage_log(request):
    if request.method == 'POST':
        # Get the form data
        product_id = request.POST.get('product')
        usage_category = request.POST.get('usage_category')
        usage_time = request.POST.get('usage_time')

        # Get the selected product
        product = SkincareProduct.objects.get(id=product_id)

        # Create a new UsageLog entry
        usage_log = UsageLog(
            product=product,
            usage_category=usage_category,
            usage_time=usage_time,
        )
        usage_log.save()

        # Redirect to the usage logs page after adding the log
        return redirect('usage_logs')  # Make sure to name your URL pattern as 'usage_logs'
    
    # If not POST, just redirect back to the usage logs page
    return redirect('usage_logs')


class ProductCreate(CreateView):
    model = SkincareProduct
    fields = '__all__'

class ProductUpdate(UpdateView):
    model = SkincareProduct
    fields = '__all__'

class ProductDelete(DeleteView):
    model = SkincareProduct
    success_url = '/skincare/all_skincare/'