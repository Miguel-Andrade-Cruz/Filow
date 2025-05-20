from users.models import Teacher, Student
from schedules.models import Schedules


def handleTeacherSchedules(request, date_request=''):

    teacher = Teacher.objects.get(user_id=request.user.id)
    
    if date_request == '':
        schedules = Schedules.objects.filter(teacher_id=teacher)
    else: 
        schedules = Schedules.objects.filter(teacher_id=teacher, begins_at_date=date_request)

    return schedules



def handleStudentSchedules(request, date_request):
    
    student = Student.objects.get(user_id=request.user.id)
    
    if date_request == '':
        schedules = Schedules.objects.filter(class_id=student.class_id)
    else:
        schedules = Schedules.objects.filter(class_id=student.class_id, begins_at_date=date_request)

    return schedules