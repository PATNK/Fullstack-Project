from django.urls import path
from . import views

urlpatterns = [
    path('uploaded/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
]