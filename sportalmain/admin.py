from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['enrollment_number','user__username','user__first_name','user__last_name'] 


admin.site.register(StudentDetails, StudentAdmin)
admin.site.register(FacultyDetails)
admin.site.register(BonafideRequest)
admin.site.register(Fees)
admin.site.register(AcademicInfo)
admin.site.register(ActivityPoints100)


