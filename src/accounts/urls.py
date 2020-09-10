from django.urls import path, include

from .views import RegisterView, Profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile'),
]