from django import forms
from .models import Schedules, TeacherToClass, Classroom
from users.models import Teacher, ClassTag, Subject


class ScheduleForm(forms.Form):
    _class = forms.ModelChoiceField(queryset=ClassTag.objects.all(), label="Class")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Subject")
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), label="Classroom")
    
    begins_at_date = forms.DateField(label="Begins at date", widget=forms.DateInput(attrs={'type': 'date'}))
    begins_at_time = forms.TimeField(label="Begins at time", widget=forms.TimeInput(attrs={'type': 'time'}))

    ends_at_date = forms.DateField(label="Ends at date", widget=forms.DateInput(attrs={'type': 'date'}))
    ends_at_time = forms.TimeField(label="Ends at time", widget=forms.TimeInput(attrs={'type': 'time'}))