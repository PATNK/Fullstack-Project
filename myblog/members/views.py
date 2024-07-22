from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import Employee
from .forms import ProfilePictureForm

def upload_profile_picture(request):
    if request . method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            #Check if a profile already esists for the user
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                form = ProfilePictureForm(request.POST, request.FILES, instance=user_profile)
            except UserProfile.DoesNotExist:
                user_profile=form.save(commit=False)
                user_profile.user = rquest.user 
            
            user_profile.save()
            return redirect('upload_success') #Redirect to the success view
    else:

        form = ProfilePictureForm()
    return render(request, 'upload_picture.html', {'form':form})

def upload_success(request):
    return render(request, 'upload_success.html')

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_successful') 
        else:
            message="Invalid username or password"
            return render(request, 'login.html', {'message':message})
    return render(request, 'login.html')

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
            form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#Creating a view for successful login
def login_successful(request):
    return render(request, 'login_successful.html')

def logout_view(request):
    logout(request)
    return redirect('login')



def members(request):
    return HttpResponse("My First Django Application")

def about(request):
    return HttpResponse("Who we are")

def services(request):
    template = loader.get_template('sample.html')
    return HttpResponse(template.render())

def contact(request):
    return HttpResponse("Contact Us")

def home(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def message(request):
    return HttpResponse("Send me the order next week")

def contact(request):
    return HttpResponse("My contact mobile number is 0804763493")

def testing(request):
    template = loader.get_template('testing.html')
    context = {

        'firstname':'Nneka',
        'lastname': 'Obumse',

        'gender':'Female',
        'address':'CBD Abuja', 
    }
    return HttpResponse(template.render(context, request))

def student_info(request):
    students =Student.objects.all().values()
    #
    #employees= Employee.objects.all().values()
    template = loader.get_template('student.html')
    context = {
        'students':students,

    }
    return HttpResponse(template.render(context, request))

def employee_info(request):
    employees = Employee.objects.all().values()
    template = loader.get_template('testing.html')
    context = {
        'employees':employees,
    }
    return HttpResponse(template.render(context, request))


    


