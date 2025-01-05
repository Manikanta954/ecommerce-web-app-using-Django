from django.http import HttpResponse
from django.shortcuts import render

from electronics.models import Electronics

# Create your views here.
def ehello(request):
    return render(request,"home.html")

def electronics_list(request):
    electronics=Electronics.objects.all() 
    return render(request,'electronics_list.html',{'ets':electronics})