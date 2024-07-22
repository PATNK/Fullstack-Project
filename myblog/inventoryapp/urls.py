from django.urls import path
from . import views


urlpatterns =[
    path('productinfo_list/', views.productinfo_list, name='productinfo_list'),
    path('add_product/', views.add_productinfo, name='add_productinfo'),
    path('<int:pk>/detail', views.productinfo_detail, name='productinfo_detail'),
    path('<int:pk>/update', views.productinfo_update, name='productinfo_update'),
    path('added/', views.productinfo_added, name='productinfo_added'),
    path('<int:pk>/delete', views.productinfo_delete, name='productinfo_delete'),

    path('', views.inventorydetails_list, name='inventorydetails_list'),
    path('add_details/', views.add_inventorydetails, name='add_inventorydetails'),
    path('<int:pk>/', views.inventorydetails_detail, name='inventorydetails_detail'),
    path('<int:pk>/update', views.inventorydetails_update, name='inventorydetails_update'),
    path('added/', views.inventorydetails_added, name='inventorydetails_added'),
    path('<int:pk>/delete', views.inventorydetails_delete, name='inventorydetails_delete'),

    path('', views.supplierinfo_list, name='supplierinfo_list'),
    path('add_supplier/', views.add_supplierinfo, name='add_supplierinfo'),
    path('<int:pk>/', views.supplierinfo_detail, name='supplierinfo_detail'),
    path('<int:pk>/update', views.supplierinfo_update, name='supplierinfo_update'),
    path('added/', views.supplierinfo_added, name='supplierinfo_added'),
    path('<int:pk>/delete', views.supplierinfo_delete, name='supplierinfo_delete'),

    path('', views.pricingdetails_list, name='pricingdetails_list'),
    path('add_pricing/', views.add_pricingdetails, name='add_pricingdetails'),
    path('<int:pk>/', views.pricingdetails_detail, name='pricingdetails_detail'),
    path('<int:pk>/update', views.pricingdetails_update, name='pricingdetails_update'),
    path('added/', views.pricingdetails_added, name='pricingdetails_added'),
    path('<int:pk>/delete', views.pricingdetails_delete, name='pricingdetails_delete'),

    
    path('', views.salesinfo_list, name='salesinfo_list'),
    path('add_sales/', views.add_salesinfo, name='add_salesinfo'),
    path('<int:pk>/', views.salesinfo_detail, name='salesinfo_detail'),
    path('<int:pk>/update', views.salesinfo_update, name='salesinfo_update'),
    path('added/', views.salesinfo_added, name='salesinfo_added'),
    path('<int:pk>/delete', views.salesinfo_delete, name='salesinfo_delete'),

] 