from django.contrib import admin
from .models import StudentDetails
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['enrollment_number','user__username','user__first_name','user__last_name'] 

admin.site.register(StudentDetails,StudentAdmin)

