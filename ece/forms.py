from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class UploadFileForm(forms.Form):
    file = forms.FileField()