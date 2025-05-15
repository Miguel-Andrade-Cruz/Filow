from django import forms
from .models import Schedules, TeacherToClass, Classroom
from users.models import Teacher, ClassTag, Subject


class ScheduleForm(forms.Form):
    _class = forms.ModelChoiceField(queryset=ClassTag.objects.all(), label="Class")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject")
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), label="Classroom")
    begins_at = forms.DateTimeField(label="Begins At", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    ends_at = forms.DateTimeField(label="Ends At", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))