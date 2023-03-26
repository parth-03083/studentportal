from django.urls import path
from . import views

urlpatterns=[
    # Static
    path('about/',views.aboutView,name='about'),

    # Student
    path('',views.index,name='index'),
    path('signup/',views.register,name='signup'),
    path('login/',views.loginView,name='login'),
    path('student-details/',views.studentDetails,name='student-details'),
    path('faculty-signup/',views.facultySignup,name='faculty-signup'),
    path('academic-details/',views.academicDetails,name='academic-details'),
    path('logout/',views.logoutView,name='logout'),
    path('bonafide-request/',views.requestBonafide,name='bonafide-request'),
    path('fees-upload/',views.feesView,name='fees-upload'),
    path('activity-points/',views.activityView,name='points-activity'),
    # Admin
    

]