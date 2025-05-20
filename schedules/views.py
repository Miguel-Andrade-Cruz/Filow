from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ScheduleForm
from .models import Schedules
from users.models import Teacher, Student

@login_required(login_url='/auth/login/')
def home(request):

  if request.method == 'POST':
    
    date_request = request.POST.get('date')
    if request.user.role == 'TCHR':

      teacher = Teacher.objects.get(user_id=request.user.id)
      if date_request == '':
        schedules = Schedules.objects.filter(teacher_id=teacher)
      else: 
        schedules = Schedules.objects.filter(teacher_id=teacher, begins_at_date=date_request)

    elif request.user.role == 'STDNT':
      student = Student.objects.get(user_id=request.user.id)
      if date_request == '':
        schedules = Schedules.objects.filter(class_id=student.class_id)
      else:
        schedules = Schedules.objects.filter(class_id=student.class_id, begins_at_date=date_request)

    if schedules == []:
      return render(request, './home_teacher.html', {
        'user': request.user.name,
        'schedules': False,
      })
    schedules = [
    {
      'teacher': schedule.teacher_id.user_id.name,
      'subject': schedule.subject_id.subject_name,
      'class': schedule.class_id.tag,
      'classroom_tag': schedule.classroom_id.tag,
      'classroom_quadrant': schedule.classroom_id.quadrant,
      'begins_at_time': schedule.begins_at_time,
      'ends_at_time': schedule.ends_at_time
    }
    for schedule in schedules
    ]

    return render(request, './home_teacher.html', {
      'user': request.user.name,
      'schedules': schedules,
    })



  if request.user.role == 'TCHR':

    teacher = Teacher.objects.get(user_id=request.user.id)
    
    schedules = Schedules.objects.filter(teacher_id=teacher)

    schedules = [
      {
        'teacher': schedule.teacher_id.user_id.name,
        'subject': schedule.subject_id.subject_name,
        'class': schedule.class_id.tag,
        'classroom_tag': schedule.classroom_id.tag,
        'classroom_quadrant': schedule.classroom_id.quadrant,
        'date': schedule.begins_at_date,
        'begins_at_time': schedule.begins_at_time,
        'ends_at_time': schedule.ends_at_time,
      }
      for schedule in schedules
    ]

    return render(request, './home_teacher.html', {
      'user': request.user.name,
      'schedules': schedules,
    })
  
  
  
  elif request.user.role == 'STDNT':

    student = Student.objects.get(user_id=request.user.id)
    schedules = Schedules.objects.filter(class_id=student.class_id)

    schedules = [
      {
        'teacher': schedule.teacher_id.user_id.name,
        'subject': schedule.subject_id.subject_name,
        'class': schedule.class_id.tag,
        'classroom_tag': schedule.classroom_id.tag,
        'classroom_quadrant': schedule.classroom_id.quadrant,
        'date': schedule.begins_at_date,
        'begins_at_time': schedule.begins_at_time,
        'ends_at_time': schedule.ends_at_time,
      }
      for schedule in schedules
    ]

    return render(request, './home_student.html', {'user': request.user.name, 'schedules': schedules})



def new_schedule(request):
  if request.method == 'POST':

    form = ScheduleForm(request.POST)
    if form.is_valid():
      
      teacher = Teacher.objects.get(user_id=request.user.id)
      schedule = Schedules(
        teacher_id=teacher,
        class_id=form.cleaned_data['_class'],
        subject_id=form.cleaned_data['subject'],
        classroom_id=form.cleaned_data['classroom'],
        begins_at_date=form.cleaned_data['begins_at_date'],
        begins_at_time=form.cleaned_data['begins_at_time'],
        ends_at_date=form.cleaned_data['ends_at_date'],
        ends_at_time=form.cleaned_data['ends_at_time'],
      )
      schedule.save()
      return render(request, './new_schedule_suceeded.html')
  else: 
    form = ScheduleForm()
  
  return render(request, './new_schedule.html', {
    'form': form,
  })