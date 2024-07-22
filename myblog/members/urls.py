from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_profile_picture
from . import views


urlpatterns = [
    path('members/', views.members, name = 'members'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contact, name = 'contact'),
    path('services/', views.services, name = 'services'),
    path('home/', views.home, name = 'home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('login_successful/', views.login_successful, name='login_successful'),
    path('logout/', views.logout_view, name='logout'),
    path('message/', views.message, name='message'),
    path('contact/', views.contact, name='contact'),
    path('testing/', views.testing, name='testing'),
    path('student_info/', views.student_info, name='student_info'),
    path('employee_info/', views.employee_info, name='employee_info'),
    path('upload/', views.upload_profile_picture, name='uploat_profile_picture'),
    path('upload-success/', views.upload_success, name='upload_success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)