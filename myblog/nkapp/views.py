from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from.forms import ProdForm
from .models import Prod

# Create your views here.

def add_prod(request):
    if request.method == 'POST':
       form= ProdForm(request.POST)
       if form. is_valid():
           form.save()
           return redirect('prod_list')
    else:
        form = ProdForm()
    return render(request, 'add_prod.html', {'form':form})
    
def prod_added(request):
    return render(request, 'prod_added.html')

def prod_list(request):
    prods = Prod.objects.all()
    return render(request, 'prod_list.html', {'prods':prods})

def prod_detail(request, pk):
    prod =get_list_or_404(Prod, pk=pk)
    return render(request, 'prod_detail.html', {'prods':prod})

def prod_update(request, pk):
    prod = get_object_or_404(Prod, pk=pk)
    if request.method =='POST':
        form = ProdForm(request.POST, instance=prod)
        if form. is_valid():
            form.save()
            return redirect('prod_detail', pk=pk)
    else:
        form=ProdForm(instance=prod)
    return render(request, 'prod_update.html')

def prod_delete(request, pkl):
    prod = get_object_or_404(Prod, pk=pk)
    if request.method =='POST':
        prod.delete()
        return redirect('prod_list')
        return render(request, 'prods/prod_confirm_delete', {'prod':prod})

    return render(request, 'prod_delete.html')
    