from django.http import HttpResponse
from django.shortcuts import render

from fashion.models import Fashion

# Create your views here.
def fhello(request):
    return HttpResponse("This is fashion page")

def fashion_list(request):
    fashion=Fashion.objects.all() 
    return render(request,'fashion_list.html',{'fsh':fashion})