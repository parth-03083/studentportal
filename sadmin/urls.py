from django.urls import path
from . import views

urlpatterns = [
    # Bonafide Functionalities 
    path('bonafide-requests/', views.bonafideRequestAdmin, name='bonafide-requests'),
    path('approve-bonafide/', views.approveBonafide, name='approve-bonafide'),
    path('reject-bonafide/', views.rejectBonaFide, name='reject-bonafide'),

    # Activity Points Functionalities
    path('activity-requests/', views.activityPointsAdmin, name='activity-requests'),
    path('approve-activity/', views.approveActivity, name='approve-activity'),
    path('reject-activity/', views.rejectActivity, name='reject-activity'),

    # Fees View
    path('fees/', views.feesAdmin, name='fees'),
]
