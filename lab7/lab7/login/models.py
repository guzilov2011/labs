from django.db import models
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(min_length = 5 , label = 'Логин')
    password = forms.CharField(min_length = 6 , widget =forms.PasswordInput, label = 'Пароль')
    password2 = forms.CharField(min_length = 6 , widget =forms.PasswordInput, label = 'Повторите ввод')
    email = forms.EmailField(max_length=255, label = 'E-mail')
    first_name = forms.CharField(max_length=255, label = 'Имя')
    last_name = forms.CharField(max_length=255, label = 'Фамилия')
    
class LoginForm(forms.Form):
    username = forms.CharField(min_length = 5 , label = 'Логин')
    password = forms.CharField(min_length = 6 , widget =forms.PasswordInput, label = 'Пароль')