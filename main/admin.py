from django.contrib import admin
from .models import TourPackage,Booking

class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')
    search_fields = ('title',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'package', 'date')
    list_filter = ('package', 'date')
    search_fields = ('name', 'email')

admin.site.register(TourPackage,TourPackageAdmin)
admin.site.register(Booking)



