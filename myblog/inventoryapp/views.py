from django.shortcuts import render
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import ProductInfoForm
from .forms import InventoryDetailsForm
from .forms import SupplierInfoForm
from .forms import PricingDetailsForm
from .forms import SalesInfoForm
from .models import ProductInfo
from .models import InventoryDetails
from .models import SupplierInfo
from .models import PricingDetails
from .models import SalesInfo


# Create your views here.
def add_productinfo(request):
    if request.method == 'POST':
        form = ProductInfoForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('productinfo_list')
    else:
        form = ProductInfoForm()
    return render(request, 'add_productinfo.html', {'form':form})

def productinfo_added(request):
    return render(request, 'productinfo_added.html')

def productinfo_list(request):
    productinfos = ProductInfo.objects.all()
    return render(request, 'productinfo_list.html', {'productinfos':productinfos})

def productinfo_detail(request, pk):
    productinfo =get_object_or_404(ProductInfo, pk=pk)
    return render(request, 'productinfo_detail.html', {'productinfo':productinfo})

def productinfo_update(request, pk):
    productinfo = get_object_or_404(ProductInfo, pk=pk)
    if request.method =='POST':
        form = ProductInfoForm(request.POST, instance=productinfo)
        if form. is_valid():
            form.save()
            return redirect('productinfo_detail', pk=pk)
    else:
        form=ProductInfoForm(instance=productinfo)
    return render(request, 'productinfo_update.html')

def productinfo_delete(request, pkl):
    productinfo = get_object_or_404(ProductInfo, pk=pk)
    if request.method =='POST':
        productinfo.delete()
        return redirect('productinfo_list')
        return render(request, 'productinfo_confirm_delete', {'productinfo':productinfo})

    return render(request, 'productinfo_delete.html')


def add_inventorydetails(request):
    if request.method == 'POST':
        form = InventoryDetailsForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('inventorydetails_list')
    else:
        form = InventoryDetailsForm()
    return render(request, 'add_inventorydetails.html', {'form':form})

def inventorydetails_added(request):
    return render(request, 'inventorydetails_added.html')

def inventorydetails_list(request):
    inventorydetail = InventoryDetails.objects.all()
    return render(request, 'inventorydetails_list.html', {'inventorydetail':inventorydetail})

def inventorydetails_detail(request, pk):
    inventorydetails =get_object_or_404(InventoryDetails, pk=pk)
    return render(request, 'inventorydetails_detail.html', {'inventorydetails':inventorydetails})

def inventorydetails_update(request, pk):
    inventorydetails = get_object_or_404(InventoryDetails, pk=pk)
    if request.method =='POST':
        form = InventoryDetailsForm(request.POST, instance=inventorydetails)
        if form. is_valid():
            form.save()
            return redirect('inventorydetails_detail', pk=pk)
    else:
        form=InventoryDetailsForm(instance=inventorydetails)
    return render(request, 'inventorydetails_update.html')

def inventorydetails_delete(request, pkl):
    inventorydetails = get_object_or_404(InventoryDetails, pk=pk)
    if request.method =='POST':
        inventorydetails.delete()
        return redirect('inventorydetails_list')
        return render(request, 'inventorydetail/inventorydetails_confirm_delete', {'inventorydetails':inventorydetails})

    return render(request, 'inventorydetails_delete.html')


def add_supplierinfo(request):
    if request.method == 'POST':
        form = SupplierInfoForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('supplierinfo_list')
    else:
        form = SupplierInfoForm()
    return render(request, 'add_supplierinfo.html', {'form':form})

def supplierinfo_added(request):
    return render(request, 'supplierinfo_added.html')

def supplierinfo_list(request):
    supplierinfos = SupplierInfo.objects.all()
    return render(request, 'supplierinfo_list.html', {'supplierinfos':supplierinfos})

def supplierinfo_detail(request, pk):
    supplierinfo =get_object_or_404(SupplierInfo, pk=pk)
    return render(request, 'supplierinfo_detail.html', {'supplierinfo':supplierinfo})

def supplierinfo_update(request, pk):
    supplierinfo = get_object_or_404(SupplierInfo, pk=pk)
    if request.method =='POST':
        form = SupplierInfoForm(request.POST, instance=supplierinfo)
        if form. is_valid():
            form.save()
            return redirect('supplierinfo_detail', pk=pk)
    else:
        form=SupplierInfoForm(instance=supplierinfo)
    return render(request, 'supplierinfo_update.html')

def supplierinfo_delete(request, pkl):
    supplierinfo = get_object_or_404(SupplierInfo, pk=pk)
    if request.method =='POST':
        supplierinfo.delete()
        return redirect('supplierinfo_list')
        return render(request, 'supplierinfos/supplierinfo_confirm_delete', {'supplierinfo':supplierinfo})

    return render(request, 'supplierinfo_delete.html')


def add_pricingdetails(request):
    if request.method == 'POST':
        form = PricingDetailsForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('pricingdetails_list')
    else:
        form = PricingDetailsForm()
    return render(request, 'add_pricingdetails.html', {'form':form})

def pricingdetails_added(request):
    return render(request, 'pricingdetails_added.html')

def pricingdetails_list(request):
    pricingdetail = PricingDetails.objects.all()
    return render(request, 'inventorydetails_list.html', {'inventorydetail':inventorydetail})

def pricingdetails_detail(request, pk):
    pricingdetails =get_object_or_404(PricingDetails, pk=pk)
    return render(request, 'pricingdetails_detail.html', {'pricingdetails':pricingdetails})

def pricingdetails_update(request, pk):
    pricingdetails = get_object_or_404(PricingDetails, pk=pk)
    if request.method =='POST':
        form = PricingDetailsForm(request.POST, instance=pricingdetails)
        if form. is_valid():
            form.save()
            return redirect('pricingdetails_detail', pk=pk)
    else:
        form=PricingDetailsForm(instance=pricingdetails)
    return render(request, 'pricingdetails_update.html')

def pricingdetails_delete(request, pkl):
    pricingdetails = get_object_or_404(PricingDetails, pk=pk)
    if request.method =='POST':
        pricingdetails.delete()
        return redirect('pricingdetails_list')
        return render(request, 'pricingdetail/pricingdetails_confirm_delete', {'pricingdetails':pricingdetails})

    return render(request, 'pricingdetails_delete.html')



def add_salesinfo(request):
    if request.method == 'POST':
        form = SalesInfoForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('salesinfo_list')
    else:
        form = SalesInfoForm()
    return render(request, 'add_salesinfo.html', {'form':form})

def salesinfo_added(request):
    return render(request, 'salesinfo_added.html')

def salesinfo_list(request):
    salesinfos = SalesInfo.objects.all()
    return render(request, 'salesinfo_list.html', {'salesinfos':salesinfos})

def salesinfo_detail(request, pk):
    salesinfo =get_object_or_404(SalesInfo, pk=pk)
    return render(request, 'salesinfo_detail.html', {'salesinfo':salesinfo})

def salesinfo_update(request, pk):
    salesinfo = get_object_or_404(SalesInfo, pk=pk)
    if request.method =='POST':
        form = SalesInfoForm(request.POST, instance=salesinfo)
        if form. is_valid():
            form.save()
            return redirect('salesinfo_detail', pk=pk)
    else:
        form=SalesInfoForm(instance=salesinfo)
    return render(request, 'salesinfo_update.html')

def salesinfo_delete(request, pkl):
    salesinfo = get_object_or_404(SalesInfo, pk=pk)
    if request.method =='POST':
        salesinfo.delete()
        return redirect('salesinfo_list')
        return render(request, 'salesinfos/salesinfo_confirm_delete', {'salesinfo':salesinfo})

    return render(request, 'salesinfo_delete.html')
