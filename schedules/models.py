from datetime import date
from django.db import models
from users.models import Teacher, ClassTag, Subject

class Classroom(models.Model):
  quadrant = models.CharField(max_length=255)
  tag = models.CharField(max_length=255)

  def __str__(self):
    return f"Classe {self.tag} - Quadrante {self.quadrant}"


class TeacherToClass(models.Model):
  teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  class_id = models.ForeignKey(ClassTag, on_delete=models.CASCADE)
 
  def __str__(self):
    return f"{self.teacher_id} - {self.class_id}"



class Schedules(models.Model):
  teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  class_id = models.ForeignKey(ClassTag, on_delete=models.CASCADE)
  subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
  classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
  
  begins_at_date = models.DateField()
  begins_at_time = models.TimeField()

  ends_at_date = models.DateField()
  ends_at_time = models.TimeField()


