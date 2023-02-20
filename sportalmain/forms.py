from django import forms
from .models import StudentDetails

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({'class': 'datepicker'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control-file'})

    def save(self, commit=True):
        student_details = super().save(commit=False)
        if commit:
            student_details.save()
        return student_details