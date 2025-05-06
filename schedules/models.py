from django.db import models
from users.models import Teacher, ClassTag, Subject

class Classroom(models.Model):
  quadrant = models.CharField(max_length=255)
  tag = models.CharField(max_length=255)


class TeacherToClass(models.Model):
  teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  class_id = models.ForeignKey(ClassTag, on_delete=models.CASCADE)


class Schedules(models.Model):
  teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  class_id = models.ForeignKey(ClassTag, on_delete=models.CASCADE)
  subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
  classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
  begins_at = models.DateField()
  ends_at = models.DateField()
