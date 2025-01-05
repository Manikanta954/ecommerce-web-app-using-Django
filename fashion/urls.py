from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fashion_list, name='fashion-list'),
    path('fashion/add/', views.fashion_add, name='fashion-add'),
    path('fashion/edit/<int:pk>/', views.fashion_edit, name='fashion-edit'),
    path('fashion/delete/<int:pk>/', views.fashion_delete, name='fashion-delete'),
]