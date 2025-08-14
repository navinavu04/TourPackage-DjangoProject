from django.contrib import admin
from .models import Vendor, TourPackage,Booking

class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','vendor','is_approved')
    list_filter = ('is_approved','vendor')
    search_fields = ['title','vendor__company_name']
    actions = ['approve_packages']

def approve_packages(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected packages have been approved.")
approve_packages.short_description = "Approve selected packages"

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'package', 'date')
    list_filter = ('package', 'date')
    search_fields = ('name', 'email')

admin.site.register(Vendor)
admin.site.register(TourPackage,TourPackageAdmin)
admin.site.register(Booking)



