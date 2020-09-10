from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Student

# Register your models here.
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

class CustomUserAdmin(UserAdmin):
    inlines = (StudentInline, )
    list_display = ('username', 'email', 'is_staff',)
    list_select_related = ('student', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)