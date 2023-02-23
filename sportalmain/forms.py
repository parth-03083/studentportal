from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        self.fields['photo'].widget.attrs.update({'class': 'form-control-file'})

    def save(self, commit=True):
        student_details = super().save(commit=False)
        if commit:
            student_details.save()
        return student_details


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1','password2', 'first_name', 'last_name')


class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class FeesForm(forms.ModelForm):
    class Meta:
        model = Fees
        exclude = ['user']

