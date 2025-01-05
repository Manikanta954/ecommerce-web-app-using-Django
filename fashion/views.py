from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from fashion.models import Fashion

# Create your views here.
def fhello(request):
    return HttpResponse("This is fashion page")

def fashion_list(request):
    fashion=Fashion.objects.all() 
    return render(request,'fashion_list.html',{'fsh':fashion})

def fashion_add(request):
    if request.method == 'POST':
        # Get data from the form
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        
        # Create new fashion product
        new_fashion = Fashion.objects.create(
            product_name=product_name,
            price=price
        )
        return redirect('fashion-list')  # Redirect to the fashion list page
    
    return render(request, 'fashion_form.html')

def fashion_edit(request, pk):
    fashion = get_object_or_404(Fashion, pk=pk)
    
    if request.method == 'POST':
        # Update the product details
        fashion.product_name = request.POST.get('product_name')
        fashion.price = request.POST.get('price')
        fashion.save()  # Save the updated details
        
        return redirect('fashion-list')  # Redirect to the fashion list page
    
    return render(request, 'fashion_form.html', {'fashion': fashion})

def fashion_delete(request, pk):
    fashion = get_object_or_404(Fashion, pk=pk)
    
    if request.method == 'POST':
        # Delete the product
        fashion.delete()
        return redirect('fashion-list')  # Redirect to the fashion list page
    
    # If the request is GET, show the confirmation page
    return render(request, 'fashion_confirm_delete.html', {'fashion': fashion})