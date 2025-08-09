from django import forms
from .models import TourPackage
from .models import Booking
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vendor

class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ['title', 'description', 'price', 'image']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VendorRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Vendor
        fields = ['company_name','username','password']



