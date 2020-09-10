from django import forms
from django.db import transaction
from django.contrib.auth import get_user_model

from .models import Student


User = get_user_model()

class StudentSignUpForm(forms.ModelForm):
    matric_number = forms.CharField()
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    department = forms.CharField()
    university = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        data = self.cleaned_data
        date_of_birth = data.get('date_of_birth')
        matric_number = data.get('matric_number')
        department = data.get('department')
        university = data.get('university')
        Student.objects.create(
            user = user,
            date_of_birth = date_of_birth,
            matric_number = matric_number,
            department = department,
            university = university
        )
        return user