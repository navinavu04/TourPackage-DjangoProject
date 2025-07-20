from django import forms
from .models import TourPackage
from .models import Booking

class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ['title', 'description', 'price', 'image']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date']
