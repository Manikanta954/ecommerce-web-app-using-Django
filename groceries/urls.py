from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.groceries_list, name='groceries-list'),
    path('groceries/add/', views.groceries_add, name='groceries-add'),
    path('groceries/edit/<int:pk>/', views.groceries_edit, name='groceries-edit'),
    path('groceries/delete/<int:pk>/', views.groceries_delete, name='groceries-delete'),
]