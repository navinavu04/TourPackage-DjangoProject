from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add/', views.add_package, name='add_package'),
    path('book/<int:package_id>/', views.book_package, name='book_package'),
]
