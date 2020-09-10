from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from .forms import StudentSignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(CreateView):
    form_class = StudentSignUpForm
    template_name = 'accounts/register.html'
    success_url = '/login'

class Profile(View):
    # model = User
    # template_name = 'accounts/user_detail.html'
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, 'accounts/user_detail.html', context)