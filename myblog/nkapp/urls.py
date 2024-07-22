from django.urls import path
from . import views


urlpatterns =[
    path('', views.prod_list, name='prod_list'),
    path('add_prod/', views.add_prod, name='add_prod'),
    path('<int:pk>/', views.prod_detail, name='prod_detail'),
    path('<int:pk>/update', views.prod_update, name='prod_update'),
    path('<int:pk>/delete', views.prod_delete, name='prod_delete'),
    path('added/', views.prod_added, name='prod_added'),
]