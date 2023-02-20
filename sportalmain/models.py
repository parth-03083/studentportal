from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class StudentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(primary_key=True, max_length=12)
    personal_email = models.EmailField()
    # institute_email = models.EmailField()
    # first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30)
    father_email = models.EmailField(blank=True)
    mother_name = models.CharField(max_length=60)
    mother_email = models.EmailField(blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    aadhar_number = models.CharField(max_length=12, unique=True)
    religion = models.CharField(max_length=20)
    caste = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20, default="Indian")
    reserve_category = models.CharField(max_length=20, blank=True)
    person_with_disability = models.CharField(max_length=20, blank=True)
    personal_mobile_no = models.CharField(max_length=15)
    parent_mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.enrollment_number
