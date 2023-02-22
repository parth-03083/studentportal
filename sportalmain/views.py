from django.shortcuts import render,redirect,reverse
from .forms import *
from .models import *
from django.http import HttpResponse,JsonResponse
import json
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request,'index.html')

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
            return redirect(reverse('index'))
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

