from django.shortcuts import render
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from.forms import CustomerForm
from .models import Customer

# Create your views here.
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form':form})

def customer_added(request):
    return render(request, 'customer_added.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers':customers})

def customer_detail(request, pk):
    customer =get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer':customer})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method =='POST':
        form = CustomerForm(request.POST, instance=customer)
        if form. is_valid():
            form.save()
            return redirect('customer_detail', pk=pk)
    else:
        form=CustomerForm(instance=customer)
    return render(request, 'customer_update.html')

def customer_delete(request, pkl):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method =='POST':
        customer.delete()
        return redirect('customer_list')
        return render(request, 'customers/customer_confirm_delete', {'customer':customer})

    return render(request, 'customer_delete.html')