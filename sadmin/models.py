from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FacultyDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BRANCH_CHOICES = [
        ('ce', 'Computer Engineering'),
        ('it', 'Information Technology Engineering'),
        ('ic', 'Instrumental and Control Engineering'),
        ('bm', 'Biomedical Engineering'),
        ('ec', 'Electornics and Communication Engineering'),
        ('rob', 'Robotics Engineering'),
        ('civil', 'Civil Engineering'),
        ('mech', 'Mechanical Engineering'),
        ('metl', 'Mettalurgy Engineering'),
    ]
    department = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    is_bonafide=models.BooleanField(default=False)
    is_fees = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.department