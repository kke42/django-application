from django import forms
from .models import UserSubmission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['name', 'email']