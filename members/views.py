from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Username or Password is incorrect, try again!"))
            return redirect('login')

    else:
        return render(request,'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out!"))
    return redirect('/')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Succesful!"))
            return redirect('/home')
    
    else:
        form = UserCreationForm()
        
    return render(request, "authenticate/register_user.html", {'form':form})