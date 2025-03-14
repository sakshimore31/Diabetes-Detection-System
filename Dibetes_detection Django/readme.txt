step 1: create project folder where python file is located
step 2: install django by "pip install django"
step 3: give title to your project name by "django-admin startproject project_name
step 4: To run the project or server "python manage.py runserver"
step 5: create a django app "python manage.py startapp app_name
step 6: To get the administration panel i.e username and password type in the hyperlink by adding "/admin" to it.
step 7: In main project go to settings.py in the code where the installed app section is add the current app you have created in the directory.
setp 8: in main project urls.py file add "path('',include("LM_app.urls")), also need to import include function
step 9: create an urls.py file in the App's directory and write this code:

from django.urls import path
from . import views
urlpatterns=[
    path('', views.index)
]

step 10: In the app's views.py file add: 
from django.shortcuts import render
from django.http import HttpResponse, request

def index(request):
    return HttpResponse("Welcome")

....run the main project to view the html response...

we can define many functions like this in views.py for example as below:
def home(request):
    return HttpResponse("This is the home page")

def help(request):
    return HttpResponse("Have any queries? ping us on our official customer service page")

def contact(request):
    return HttpResponse("For any work related enquires, contact us.")

and we need to update urls.py like this when we add those functions:

    path('', views.index),
    path('home/', views.home),
    path('help/', views.help),
    path('contact/', views.contact),

step 11: create html templates in the main directory by creating new folder named "templates" in settings.py of main project where the template section is add: 
"DIRS": [os.path.join(BASE_DIR,"templates")], 
step 12: write down gtml code in templates and save it. And in views.py add index function and render it which will show the html page: 
def index(request):
    return render(request,"index.html")
step 13: create static files for storing the static files i.e. css, js. in settings.py add :
STATIC_URL = "static/" this is imp which we have to add settings.py file

STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
)

step 14: run these commands to use the django tables :
python manage.py makemigrations and
 python manage.py migrate

step 15: create forms.py in LM_app and where the form tag is located add method="post" and save
write this code:

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model= User
        fields = ['firstname','lastname','email','password','phone']

step 15: make changes in view.py as follows:
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .forms import RegisterForm


def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            #login(request,user)
    #return render(request,'registration.html')

def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    return render(request,'logout.html')


step 16: add this code in index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="static/style.css">
    <title>Library Management System | Registration</title>
    
</head>
<body>
    
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Email</th>
                <th>Password</th>
                <th>Phone</th>
            </tr>
        </thead>
    </table> 

    {%for Members in register%}
    <tr>
        <td>{{member.Firstname}}</td>
        <td>{{member.Lastname}}</td>
        <td>{{member.Email}}</td>
        <td>{{member.Password}}</td>
        <td>{{member.Phone}}</td>
        <td>
            <a href="" class="btn btn-warning btn-sm">Update</a>
            <a href="" class="btn btn-danger btn-sm">Delete</a>
        </td>
        {% endfor %}
    </tr>

</body>
</html>

updated index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    {% load static %}
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <title>Library Management System | Registration</title>
</head>
<body>
    
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Email</th>
                <th>Password</th>
                <th>Phone</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for mem in mem %}
            <tr>
                <td>{{ mem.Firstname }}</td>
                <td>{{ mem.Lastname }}</td>
                <td>{{ mem.Email }}</td>
                <td>{{ mem.Password }}</td>
                <td>{{ mem.Phone }}</td>
                <td>
                    <a href="/update/{{ mem.id }}" class="btn btn-warning btn-sm">Update</a>
                    <a href="" class="btn btn-danger btn-sm">Delete</a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table> 

</body>
</html>


step 17: 1. create update.html and paste the registration form code, and update the code in input filed by adding=>
 <value="{{form.Firstname.value}}"required>
in this step we have done activation of update and delete function
2.add update and delete function code in views.py 
3. add this path in urls.py 
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
4. In index.py add in the space of href: /update/{{ mem.id }} and /delete/{{ mem.id }}
and run the project.


step 18: 1.to create filter for filtering the users make filter.html:
<!-- Registration Form -->
        <div class="form-box">
            <div class="register-container" id="register">
                <div class="top">
                    <span>Have an account? <a href="#" onclick="login()">Login</a></span>
                    <header>Sign Up</header>
                </div>
                <form method="GET">
                    {% csrf_token %}
                    <div class="two-forms">
                        <div class="input-box">
                            <input type="text" class="input-field" name="Firstname" id="Firstname" placeholder="Firstname" value="{{ request.GET.Firstname }}">
                            <i class="bx bx-user"></i>
                        </div>
                        <div class="input-box">
                            <input type="text" class="input-field" name="Lastname" id="Lastname" placeholder="Lastname" value="{{ request.GET.Lastname }}">
                            <i class="bx bx-user"></i>
                        </div>
                    </div>
                    <div class="input-box">
                        <input type="text" class="input-field" name="Email" id="Email" placeholder="Email" value="{{ request.GET.Email }}">
                        <i class="bx bx-envelope"></i>
                    </div>
                    <div class="input-box">
                        <input type="password" class="input-field" name="Password" id="Password" placeholder="Password" value="{{ request.GET.Password }}">
                        <i class="bx bx-lock-alt"></i>
                    </div>
                    <div class="input-box">
                        <input type="text" class="input-field" name="Phone" id="Phone" placeholder="Phone" value="{{ request.GET.Phone }}">
                        <i class="bx bx-phone"></i> 
                    </div>
                    <div class="input-box">
                        <input type="submit" class="submit" value="Register">
                    </div>
                    <div class="two-col">
                        <div class="one">
                            <input type="checkbox" id="register-check">
                            <label for="register-check"> Remember Me</label>
                        </div>
                        <div class="two">
                            <label><a href="#">Terms & conditions</a></label>
                        </div>
                    </div>
                </form>
                
                <!-- Table for Members -->
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Firstname</th>
                            <th>Lastname</th>
                            <th>Email</th>
                            <th>Password</th>
                            <th>Phone</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for mem in mem %}
                        <tr>
                            <td>{{ mem.Firstname }}</td>
                            <td>{{ mem.Lastname }}</td>
                            <td>{{ mem.Email }}</td>
                            <td>{{ mem.Password }}</td>
                            <td>{{ mem.Phone }}</td>
                            <td>
                                <a href="/filter" class="btn btn-info btn-sm">Filter</a>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody> 
                </table>
            </div>
        </div>
    </div>

2.also make changes in view.py and urls.py accordingly by creating function filter:
def filter(request):
    mem = register.objects.all()

    # Get query parameters
    Firstname_query = request.GET.get('Firstname')
    Lastname_query = request.GET.get('Lastname')
    Email_query = request.GET.get('Email')
    Password_query = request.GET.get('Password')
    Phone_query = request.GET.get('Phone')

    # Apply filters
    if Firstname_query:
        mem = mem.filter(Firstname__icontains=Firstname_query)
    if Lastname_query:
        mem = mem.filter(Lastname__icontains=Lastname_query)
    if Email_query:
        mem = mem.filter(Email__icontains=Email_query)
    if Password_query:
        mem = mem.filter(Password__icontains=Password_query)
    if Phone_query:
        mem = mem.filter(Phone__icontains=Phone_query)
    
    return render(request, 'filter.html', {'mem': mem})

3.add the href in index.html:
<a href="/filter" class="btn btn-info btn-sm">Filter</a>

step 18: to create super user run the following command
python manage.py createsuperuser




