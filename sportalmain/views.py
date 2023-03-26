from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse,JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        try:
            student_details = StudentDetails.objects.get(user=request.user) 
            academic_details = AcademicInfo.objects.get(user=student_details)
            if student_details and academic_details: 
                context = {'student_details':student_details,'academic_details':academic_details, 'headers': True  }
            else:
                context = {'headers': False}
            return render(request,'home.html',context)
        except student_details.DoesNotExist:
           return redirect('student-details')
        except academic_details.DoesNotExist:
              return redirect('academic-details')
    


def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)

        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            user = User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)
            user=authenticate(request,username=email,password=password)
            login(request,user=user)
            print(user)
            # return redirect(reverse('index'))
        else:
            return HttpResponse('Invalid form',form.errors) 
    context={'form':SignUp()}
    return render(request,'register.html',context)


def loginView(request):
    if request.method == 'POST':
        email=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user=user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('Invalid credentials')
    return render(request,'login.html')


def studentDetails(request):
    form = StudentDetailsForm()
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            student_details = form.save(commit=False)
            student_details.user = request.user
            student_details.save()
            return redirect(reverse('index'))
        else:
            return HttpResponse('Invalid form')
    context = {'form':form}
    return render(request,'student-details.html',context)


def requestBonafide(request):
    student_user = StudentDetails.objects.get(user=request.user)
    if not student_user:
        return redirect('student-details')
    else:
        bonafide_objects = BonafideRequest.objects.filter(user=student_user)
        form = BonafideRequestForm()
        if request.method == 'POST':
            form = BonafideRequestForm(request.POST)
            if form.is_valid():
                bonafide = form.save(commit=False)
                student_user = StudentDetails.objects.get(user=request.user)
                if student_user:
                    bonafide.user = student_user
                    bonafide.save()
                    return redirect(reverse('index'))
                else:
                    return redirect('student-details')
            else:
                return HttpResponse('Invalid form')
        context = {'form':form,'bonafide_objects':bonafide_objects}
        return render(request,'bonafide-request.html',context)


def facultySignup(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            user = User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)
            user=authenticate(request,username=email,password=password)
            login(request,user=user)
            print(user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('Invalid form',form.errors)
    context = {'form':form}
    return render(request,'faculty-signup.html',context)

def academicDetails(request):
    form = AcademicInfoForm()
    if request.method == 'POST':
        form = AcademicInfoForm(request.POST)
        if form.is_valid():
            student_details = form.save(commit=False)
            student_user = StudentDetails.objects.get(user=request.user)
            if student_user:
                student_details.user = student_user
                student_details.save()
                return redirect('index')
            else:
                return redirect('student-details')
        else:
            return HttpResponse('Invalid form')
    context = {'form':form}
    return render(request,'academic-details.html',context)

def logoutView(request):
    logout(request)
    return redirect(reverse('login'))

def feesView(request):
    fees_objects = Fees.objects.filter(user=StudentDetails.objects.get(user=request.user))
    form = FeesForm()
    if request.method == 'POST':
        form = FeesForm(request.POST)
        if form.is_valid():
            fees = form.save(commit=False)
            student_user =StudentDetails.objects.get(user=request.user)
            if student_user:
                fees.user = student_user
                fees.save()
                return redirect('index')
            else:
                return redirect('student-details') 
        
        else:
            return HttpResponse('Invalid form')
    context = {'form':form,'fees_objects':fees_objects}
    return render(request,'fees.html',context)

def activityView(request):
    activity_objects = ActivityPoints100.objects.filter(user=StudentDetails.objects.get(user=request.user))
    form = ActivityForm()
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            student_user = StudentDetails.objects.get(user=request.user)
            if student_user:
                activity.user = student_user
                activity.save()
                return redirect(reverse('index'))
            else:
                return redirect('student-details')
        else:
            return HttpResponse('Invalid form')
    context = {'form':form , 'activity_objects':activity_objects}
    return render(request,'activity.html',context)

def aboutView(request):
    return render(request,'about.html')