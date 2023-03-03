from django.shortcuts import render,redirect
from sportalmain.forms import *
from .models import *
from sportalmain.models import BonafideRequest , ActivityPoints100
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def bonafideRequestAdmin(request):
    if request.user.is_authenticated:
        faculty = FacultyDetails.objects.get(user=request.user)
        if faculty.is_bonafide:
            bonafide_object = BonafideRequest.objects.filter(user__current_branch=faculty.department,status='pending')
            print(bonafide_object)
            return render(request,'admin_bonafide_requests.html',{'bonafide_object':bonafide_object})    
        else:
            return HttpResponse("You are not allowed to view this page")
    else:
        return redirect('login')

def approveBonafide(request):
    if request.method=='POST':
        id = request.POST.get('id')
        bonafide_object = BonafideRequest.objects.get(id=id)
        bonafide_object.status = 'approved'
        bonafide_object.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})

def rejectBonaFide(request):
    if request.method=='POST':
        id = request.POST.get('id')
        bonafide_object = BonafideRequest.objects.get(id=id)
        bonafide_object.status = 'rejected'
        bonafide_object.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})

def activityPointsAdmin(request):
    if request.user.is_authenticated:
        faculty = FacultyDetails.objects.get(user=request.user)
        if faculty.is_activity:
            activity_object = ActivityPoints100.objects.filter(user__current_branch=faculty.department,status='pending')
            print(activity_object)
            return render(request,'admin_activity_points.html',{'activity_object':activity_object})    
        else:
            return HttpResponse("You are not allowed to view this page")
    else:
        return redirect('login')
    
def approveActivity(request):
    if request.method=='POST':
        id = request.POST.get('id')
        activity_object = ActivityPoints100.objects.get(id=id)
        activity_object.status = 'approved'
        activity_object.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})
    
def rejectActivity(request):
    if request.method=='POST':
        id = request.POST.get('id')
        activity_object = ActivityPoints100.objects.get(id=id)
        activity_object.status = 'rejected'
        activity_object.save()
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})

def feesAdmin(request):
    if request.user.is_authenticated:
        faculty = FacultyDetails.objects.get(user=request.user)
        if faculty.is_fees:
            fees_object = Fees.objects.filter(user__current_branch=faculty.department)
            return render(request,'admin_fees.html',{'fees_object':fees_object})    
        else:
            return HttpResponse("You are not allowed to view this page")
    else:
        return redirect('login')

