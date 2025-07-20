from django.shortcuts import render,redirect,get_object_or_404
from .models import TourPackage , Booking
from .forms import TourPackageForm
from .forms import BookingForm


def home(request):
    packages = TourPackage.objects.all()
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
    package = get_object_or_404(TourPackage, id=package_id)
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

