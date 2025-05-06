from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def home(request):
  if request.user.role == 'TCHR':



    return render(request, 'schedules/home_teacher.html', {'user': request.user.name})
  
  
  
  
  
  
  elif request.user.role == 'STDNT':

    
    return render(request, './home_student.html', {'user': request.user.name})
 