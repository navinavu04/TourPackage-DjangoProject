from django.urls import path
from . import views

urlpatterns = [
    # User routes
    path('', views.index, name='index'),  
    path('home/', views.home, name='home'), 
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('book/<int:package_id>/', views.book_package, name='book_package'),

    # Vendor routes
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    path('vendor/login/', views.vendor_login, name='vendor_login'),
    path('vendor/logout/', views.vendor_logout, name='vendor_logout'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/package/add/', views.add_package_vendor, name='vendor_add_package'),
    path('vendor/package/edit/<int:package_id>/', views.edit_package_vendor, name='edit_package_vendor'),
    path('vendor/package/delete/<int:package_id>/', views.delete_package_vendor, name='delete_package_vendor'),

    path('choose_login/',views.choose_login,name='choose_login'),
]