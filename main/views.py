from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout,login as auth_login
from django.contrib import messages
from .models import TourPackage, Vendor
from .forms import TourPackageForm, UserRegisterForm, VendorRegistrationForm
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('user_dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
           return render(request,'main/login.html',{'error':'Invalid username or password'})
    return render(request, 'main/login.html')

def user_dashboard(request):
    packages = TourPackage.objects.filter(is_approved=True)
    return render(request, 'main/user_dashboard.html', {'packages':packages})

def home(request):
    packages = TourPackage.objects.filter(is_approved=True)
    return render(request, 'main/home.html', {'packages': packages})

def add_package(request):
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = TourPackageForm()
    return render(request, 'main/add_package.html', {'form': form})

def book_package(request, package_id):
    package = get_object_or_404(TourPackage, id=package_id,is_approved=True)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            booking.save()
            print("Booking confirmed for:", form.cleaned_data)
            return render(request, 'main/booking_success.html', {'package': package, 'user_name': form.cleaned_data.get('name'), 'user_email': form.cleaned_data.get('email')})
    else:
        form = BookingForm()
    return render(request, 'main/book.html', {'package': package,'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')  


def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            company_name = form.cleaned_data['company_name']
            contact = form.cleaned_data['contact']

            
            if User.objects.filter(username=username).exists():
                return render(request, 'main/vendor_register.html', {
                    'form': form,
                    'error': 'Username already exists. Please choose a different one.'
                })

            
            user = User.objects.create_user(username=username, password=password)
            vendor = Vendor.objects.create(user=user, company_name=company_name, contact=contact)

            return render(request, 'main/vendor_register_success.html', {'vendor': vendor})
    else:
        form = VendorRegistrationForm()

    return render(request, 'main/vendor_register.html', {'form': form})

def vendor_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            try:
                vendor = Vendor.objects.get(user=user)
                if vendor.is_approved:
                    login(request, user)
                    return redirect('vendor_dashboard')
                else:
                    return render(request, 'main/vendor_login.html', {'error': 'Account not approved yet.'})
            except Vendor.DoesNotExist:
                return render(request, 'main/vendor_login.html', {'error': 'Not a registered vendor.'})
        else:
            return render(request, 'main/vendor_login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/vendor_login.html')

def vendor_dashboard(request):
    vendor = Vendor.objects.get(user=request.user)
    packages = TourPackage.objects.filter(vendor=request.user.vendor)
    return render(request, 'main/vendor_dashboard.html', {'packages': packages})

def add_package_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.vendor = vendor   
            package.is_approved = False    
            package.save()
            return redirect('vendor_dashboard')
    else:
        form = TourPackageForm()
    return render(request, 'main/add_package_vendor.html', {'form': form})

def edit_package_vendor(request, package_id):
    package = get_object_or_404(TourPackage, id=package_id, vendor__user=request.user)
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('vendor_dashboard')
    else:
        form = TourPackageForm(instance=package)
    return render(request, 'main/edit_package_vendor.html', {'form': form})


def delete_package_vendor(request, package_id):
    package = get_object_or_404(TourPackage, id=package_id, vendor__user=request.user)
    package.delete()
    return redirect('vendor_dashboard')

def vendor_logout(request):
    logout(request)
    return redirect('index') 

def choose_login(request):
    return render(request,'main/choose_login.html')
