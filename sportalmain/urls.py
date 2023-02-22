from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.register,name='signup'),
    path('login',views.loginView,name='login'),
    path('student-details',views.studentDetails,name='student-details'),
]