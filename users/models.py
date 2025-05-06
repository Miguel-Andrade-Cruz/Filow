from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
  
  def create_user(self, name, email, role, password=None):
    if not email:
      raise ValueError('The Email field must be set')
    if not role:
      raise ValueError('The Role field must be set')
    
    hashed_password = make_password(password)
    user = User(name=name, email=email, role=role, password=hashed_password)
    user.save(using=self._db)
    return user

  def create_superuser(self, name, email, role='ADMIN', password=None):
    user = self.create_user(name, email, role, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  ROLES = {
    'STDNT': 'Student',
    'TCHR': 'Teacher',
    'ADMIN': 'Administrator'
  }
  email = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  role = models.CharField(choices=ROLES.items(), max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name", "role"]

  objects = UserManager()

  def has_perm(self, perm, obj=None):
    return self.is_superuser

  def has_module_perms(self, app_label):
    return self.is_superuser
  
class Subject(models.Model):
  subject_name = models.CharField(max_length=255)


class ClassTag(models.Model):
  tag = models.CharField(max_length=255)


class Teacher(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Student(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  class_id = models.ForeignKey(ClassTag, on_delete=models.CASCADE)

