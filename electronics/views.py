from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

from electronics.models import Electronics

# Create your views here.
def ehello(request):
    return render(request,"home.html")

def electronics_list(request):
    electronics=Electronics.objects.all() 
    return render(request,'electronics_list.html',{'ets':electronics})

def electronics_edit(request, pk):
    # Fetch the electronics item by primary key (ID)
    electronics = get_object_or_404(Electronics, pk=pk)

    if request.method == 'POST':
        # Update the electronics details
        electronics.product_name = request.POST.get('product_name')  # e.g., Product name
        electronics.price = request.POST.get('price')  # e.g., Price of the item
        electronics.save()  # Save changes to the database

        # Redirect to the electronics list view after editing
        return redirect('electronics-list')  # Use the name you assigned to the electronics list URL

    # If it's a GET request, render the form with the existing data
    return render(request, 'electronics_form.html', {'electronics': electronics})

def electronics_add(request):
    if request.method == 'POST':
        
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        
        
        new_electronics = Electronics.objects.create(
            product_name=product_name,
            price=price
        )
        return redirect('electronics-list')
    
    return render(request, 'electronics_form.html')

def electronics_delete(request, pk):
    
    electronics = get_object_or_404(Electronics, pk=pk)
    
    if request.method == 'POST':
        
        electronics.delete()
        return redirect('electronics-list') 
    

    return render(request, 'electronics_confirm_delete.html', {'electronics': electronics})