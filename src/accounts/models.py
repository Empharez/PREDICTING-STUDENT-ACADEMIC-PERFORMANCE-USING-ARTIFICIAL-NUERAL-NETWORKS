from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=40)
    university = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#         instance.profile.save()
