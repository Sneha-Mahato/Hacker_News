from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests


def home(request):
    return render(request, 'static.html')

def login(request):
    if request.method == 'POST':
        username1 = request.POST['User_name']
        password1 = request.POST['password']
        from django.contrib import auth
        x = auth.authenticate(User_name=username1,password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('/')

    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        User_name = request.POST['User_name']
        Email = request.POST['Email']
        password = request.POST['password']

        x=User.objects.create_user(User_name=User_name, Email=Email, password=password)
        x.save()
        print("USER CREATED")
        return redirect('static.html')


    else:
         return render(request, 'signup.html')


'''def home(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=12c7ca59e3ad4853b432c22449cda531')
    output = response.json()


    return render(request, 'home.html', {"articles": output['articles']})'''