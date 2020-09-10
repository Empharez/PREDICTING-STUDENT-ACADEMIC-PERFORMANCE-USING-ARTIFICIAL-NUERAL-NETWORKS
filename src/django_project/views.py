from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
# from django.contrib.auth.forms import UserCreationForm
from .forms import StudentSignUpForm

class RegisterView(CreateView):
    form_class = StudentSignUpForm
    template_name = 'accounts/register.html'
    success_url = '/login'