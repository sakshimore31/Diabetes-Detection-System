from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('login')  
    else:
        form = RegisterForm()  
    
    return render(request, 'registration.html', {'form': form})  

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user= authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('predict')
    else:
        form= AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def predict(request):
    return render(request, 'predict.html')


def result(request):
    if request.method == 'POST':
        glucose = request.POST['glucose']
        bloodPressure = request.POST['bloodPressure']
        skinThickness = request.POST['skinThickness']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        diabetesPedigreeFunction = request.POST['diabetesPedigreeFunction']
        age = request.POST['age']

        lis = [glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]
        print(lis)

        from joblib import load
        model = load(r'C:\Users\HP\.spyder-py3\Dibetes_detection\model.joblib')

        result = model.predict([lis])
        print(result)

        if result[0] == 0:
            print("No")
            value = 'Negative'
        else:
            print('Yes')
            value = 'Positive'
        
        # Return the result if POST request
        return render(request, 'result.html', {
            'ans': value,
            'title': 'Predict'
        })
    else:
        # Default behavior when not POST (optional, based on your use case)
        return render(request, 'predict.html')

def display_csv(request):
    # Load the CSV file
    csv_file_path = "C:/Users/HP/OneDrive/Desktop/Python Projects/Dibetes_detection/Diabetes_project/Diabetics_App/diabetes.csv"  # Ensure the path is correct

    # Prepare an empty list to hold the CSV data
    data = []
    headers = []

    # Open and read the CSV file
    with open("diabetes.csv", newline='') as csvfile:  # Use the variable, not the string
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Read the first row as headers
        for row in csvreader:
            data.append(row)

    # Pass headers and data to the template
    context = {
        'headers': headers,
        'data': data,
    }

    return render(request, 'display_csv.html', context)


def logout(request):
    return render(request, 'logout.html')
