from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import SkincareProduct, UsageLog
from django.utils import timezone



# Define the home view function
class Home(LoginView):
  template_name = 'home.html'

@login_required
def all_skincare(request):
    skincare_products = SkincareProduct.objects.filter(user=request.user)
    return render(request, 'skincare/all_skincare.html', {'skincare_products': skincare_products})

def morning(request):
    skincare_products = SkincareProduct.objects.filter(user=request.user)
    # for product in skincare_products:
    #     product.image_url = f"{product.image}"
    return render(request, 'skincare/morning.html', {'skincare_products': skincare_products})

def evening(request):
    skincare_products = SkincareProduct.objects.filter(user=request.user)
    return render(request, 'skincare/evening.html', {'skincare_products': skincare_products})

def weekly(request):
    skincare_products = SkincareProduct.objects.filter(user=request.user)
    return render(request, 'skincare/weekly.html', {'skincare_products': skincare_products})

def sera_skincare(request):
    return render(request, 'skincare/sera_skincare.html')

@login_required
def product_detail(request, product_id):

    skincare_product = get_object_or_404(SkincareProduct, id=product_id)
    
    usage_logs = UsageLog.objects.filter(product=skincare_product).order_by('-usage_time')

    if request.method == 'POST':
        # get the data from the form
        usage_category = request.POST.get('usage_category')
        usage_date = request.POST.get('usage_date')
        usage_time = request.POST.get('usage_time')

        # combine date and time
        usage_datetime = timezone.make_aware(
            timezone.datetime.strptime(f"{usage_date} {usage_time}", "%Y-%m-%d %H:%M")
        )

        # create new usage log for the selected product
        UsageLog.objects.create(
            product=skincare_product,
            usage_category=usage_category,
            usage_time=usage_datetime,
        )

        # redirect to see the updated logs
        return redirect('product_detail', product_id=product_id)

    # just display the page if its a get req
    return render(request, 'skincare/product_detail.html', {
        'product': skincare_product,
        'usage_logs': usage_logs,
    })


def usage_logs(request):
    # get all usage logs, ordered by most recent
    usage_logs = UsageLog.objects.all().order_by('-usage_time')

    # get current date and find the start of the current week (Monday)
    start_of_week = timezone.now() - timezone.timedelta(days=timezone.now().weekday())

    # create list of days of the week (0 to 6) starting from Monday
    days_of_week = [start_of_week + timezone.timedelta(days=i) for i in range(7)]

    skincare_products = SkincareProduct.objects.all()

    # pass data to the template
    context = {
        'usage_logs': usage_logs,
        'days_of_week': days_of_week,
        'skincare_products': skincare_products,
    }

    return render(request, 'logs/usage_logs.html', context)

@login_required
def add_usage_log(request):
    if request.method == 'POST':
        # grab the form data
        product_id = request.POST.get('product')
        usage_category = request.POST.get('usage_category')
        usage_time = request.POST.get('usage_time')

        product = SkincareProduct.objects.get(id=product_id)

        # create a new UsageLog entry
        usage_log = UsageLog(
            product=product,
            usage_category=usage_category,
            usage_time=usage_time,
        )
        usage_log.save()

        return redirect('usage_logs')
    
    # ff not POST, just redirect back to the usage logs page
    return redirect('usage_logs')


class ProductCreate(LoginRequiredMixin, CreateView):
    model = SkincareProduct
    fields = ['name', 'brand', 'benefits', 'value', 'category'] 

    def form_valid(self, form):
        # assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # let the CreateView do its job as usual
        return super().form_valid(form)

class ProductUpdate(UpdateView):
    model = SkincareProduct
    fields = '__all__'

class ProductDelete(DeleteView):
    model = SkincareProduct
    success_url = '/skincare/all_skincare/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            # redirect to home
            return redirect('home')  
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
