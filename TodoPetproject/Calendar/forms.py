from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'Priorities', 'group', 'status', 'deadline']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'group']