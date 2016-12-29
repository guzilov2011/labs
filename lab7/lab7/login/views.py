from django.shortcuts import render
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.views import View
from login.models import *
from login.forms import *

def registration(request):

    if request.user.is_authenticated():
        return render(request, 'loggedin.html')

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return render(request, 'registered.html')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {
        'form': form
    })


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            return render(request, 'loggedin.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })

def loggedin(request):
    return render(request, 'loggedin.html')
