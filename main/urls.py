from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.user_register, name='user_register'),
    path('login/',views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('',views.home, name='home'),
    path('add/', views.add_package, name='add_package'),
    path('book/<int:package_id>/', views.book_package, name='book_package'),
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    path('vendor/login/', views.vendor_login, name='vendor_login'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/edit-package/<int:pk>/', views.edit_package_vendor, name='edit_package'),
    path('vendor/delete-package/<int:pk>/', views.delete_package_vendor, name='delete_package'),
    path('vendor/package/add/', views.add_package_vendor, name='add_package_vendor'),
    path('vendor/package/edit/<int:package_id>/', views.edit_package_vendor, name='edit_package_vendor'),
    path('vendor/package/delete/<int:package_id>/', views.delete_package_vendor, name='delete_package_vendor'),  
]

