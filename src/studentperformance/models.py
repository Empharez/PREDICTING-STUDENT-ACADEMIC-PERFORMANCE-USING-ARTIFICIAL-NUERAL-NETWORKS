from django.shortcuts import reverse
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

User = settings.AUTH_USER_MODEL


class Performance(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female')
    )

    RANGE_1 = (
        (1, 'Very Low'), 
        (2, 'Low'),
        (3, 'Moderate'),
        (4, 'High'),
        (5, 'Very High')
    )

    STUDY_TIME_CHOICES = (
        (1, '> 2 hours'),
        (2, '2 to 5 hours'), 
        (3, '5 to 10 hours'), 
        (4, '< 10 hours')
    )

    student             = models.ForeignKey(User, on_delete=models.CASCADE)
    age                 = models.PositiveIntegerField(help_text='You must be btw 16-29', validators=[MinValueValidator(16), MaxValueValidator(29),])
    study_time          = models.PositiveIntegerField(choices=STUDY_TIME_CHOICES)
    activities          = models.BooleanField(verbose_name='Are you involved in Extra-curricular activities', default=False)
    higher_edu          = models.BooleanField(verbose_name="Do you intend to pursue an higher education?", default=False)
    freetime_level      = models.PositiveIntegerField(choices=RANGE_1)
    outing_level        = models.PositiveIntegerField(choices=RANGE_1) 
    weekend_alcohol_level   = models.PositiveIntegerField(choices=RANGE_1)
    health_status       = models.PositiveIntegerField(choices=RANGE_1)
    absent_weeks        = models.PositiveIntegerField(help_text='Must not be more than 6 weeks', validators=[MaxValueValidator(6),])
    gp1                 = models.DecimalField(help_text='First Semester GP range(0-4.00)', decimal_places=2, max_digits=3, validators=[MaxValueValidator(4.00),])
    gp2                 = models.DecimalField(help_text='Second Semester GP range(0-4.00)', decimal_places=2, max_digits=3, validators=[MaxValueValidator(4.00),])
    predicted_class     = models.CharField(max_length=10)
    recorded_on         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username
    
    def get_absolute_url(self):
        return reverse("performance_detail", kwargs={"pk": self.pk})
    