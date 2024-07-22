from django.urls import path
from . import views


urlpatterns =[
    path('', views.customer_list, name='customer_list'),
    path('add/', views.add_customer, name='add_customer'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('<int:pk>/update', views.customer_update, name='customer_update'),
    path('<int:pk>/delete', views.customer_delete, name='customer_delete'),
    path('added/', views.customer_added, name='customer_added'),
]