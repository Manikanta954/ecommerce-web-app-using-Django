from django.http import HttpResponse
from django.shortcuts import render

from groceries.models import Groceries

# Create your views here.
def ghello(request):
    return HttpResponse("This is groceries page")

def groceries_list(request):
    groceries=Groceries.objects.all() 
    return render(request,'groceries_list.html',{'grc':groceries})