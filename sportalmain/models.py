# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
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
    BLOOD_TYPE=[
        ('bp','B+'),
        ('bn','B-'),
        ('ap','A+'),
        ('an','A-'),
        ('op','O+'),
        ('on','O-'),
        ('abp','AB+'),
        ('abn','AB-'),
    ]
    blood_group = models.CharField(choices=BLOOD_TYPE,max_length=5, blank=True)
    GENDER_TYPE=[
        ('male','Male'),
        ('female','Female')
    ]
    gender = models.CharField(choices=GENDER_TYPE,max_length=10)
    date_of_birth = models.DateField()
    aadhar_number = models.CharField(max_length=12, unique=True)
    religion = models.CharField(max_length=20)
    caste = models.CharField(max_length=20)
    NATIONALITY_TYPE=[
        ('indian','Indian'),
        ('nri','NRI'),
    ]
    nationality = models.CharField(choices=NATIONALITY_TYPE,max_length=20, default=1)

    reserve_category = models.BooleanField(max_length=20, blank=True)
    person_with_disability = models.BooleanField(max_length=20, blank=True)
    personal_mobile_no = models.CharField(max_length=15)
    parent_mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.enrollment_number


class AcademicInfo(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=10)
    admission_type = models.CharField(max_length=10)
    date = models.DateField()
    quota = models.CharField(max_length=20)
    ews = models.BooleanField()
    ssc = models.FloatField()
    STREAM_TYPE = [
        ('hsc', 'HSC'),
        ('diploma', 'Diploma'),
    ]
    stream = models.CharField(max_length=10, choices=STREAM_TYPE)
    hsc_result = models.FloatField()
    hsc_board = models.CharField(max_length=50)
    university_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    cgpa = models.FloatField()
    COURSE_CHOICES = [
        ('be', 'BE'),
        ('me', 'ME')
    ]
    current_course = models.CharField(max_length=5, choices=COURSE_CHOICES)
    current_semester = models.IntegerField(validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ])
    BRANCH_CHOICES = [
        ('ce', 'Computer'),
        ('it', 'Information Technology'),
        ('ic', 'Instrumental and Control'),
        ('bm', 'Biomedical'),
        ('ec', 'Electornics and Communication'),
        ('rob', 'Robotics'),
        ('civil', 'Civil'),
        ('mech', 'Mechanical'),
        ('metl', 'Mettalurgy'),
    ]
    current_branch = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email


class Fees(models.Model):
    DUI = models.CharField(max_length=12)
    semester = models.IntegerField(validators=[
        MaxValueValidator(8),
        MinValueValidator(1)
    ])
    fees_type = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to='fees/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fees_type} - {self.semester}'




