from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ehello),
    path('electronics/', views.electronics_list, name='electronics-list'),
    path('electronics/add/', views.electronics_add, name='electronics-add'),  # Add this line
    path('electronics/edit/<int:pk>/', views.electronics_edit, name='electronics-edit'),
    path('electronics/delete/<int:pk>/', views.electronics_delete, name='electronics-delete'),
]
