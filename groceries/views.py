from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from groceries.models import Groceries

# Create your views here.
def ghello(request):
    return HttpResponse("This is groceries page")

def groceries_list(request):
    groceries=Groceries.objects.all() 
    return render(request,'groceries_list.html',{'grc':groceries})

def groceries_add(request):
    if request.method == 'POST':
        # Get data from the form
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        # Create a new groceries product
        new_grocery = Groceries.objects.create(
            product_name=product_name,
            price=price,
            quantity=quantity
        )
        return redirect('groceries-list')  # Redirect to the groceries list page
    
    return render(request, 'groceries_form.html')

def groceries_edit(request, pk):
    grocery = get_object_or_404(Groceries, pk=pk)
    
    if request.method == 'POST':
        # Update the product details
        grocery.product_name = request.POST.get('product_name')
        grocery.price = request.POST.get('price')
        grocery.quantity = request.POST.get('quantity')
        grocery.save()  # Save the updated details
        
        return redirect('groceries-list')  # Redirect to the groceries list page
    
    return render(request, 'groceries_form.html', {'grocery': grocery})
def groceries_delete(request, pk):
    grocery = get_object_or_404(Groceries, pk=pk)
    
    if request.method == 'POST':
        # Delete the product
        grocery.delete()
        return redirect('groceries-list')  # Redirect to the groceries list page
    
    # If the request is GET, show the confirmation page
    return render(request, 'groceries_confirm_delete.html', {'grocery': grocery})