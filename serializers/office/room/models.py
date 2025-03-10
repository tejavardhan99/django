from django.db import models
from django.contrib.auth.hashers import make_password

class School(models.Model):
    school_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    objects=models.Manager()
    class Meta:
        db_table="school_table"




class Teacher(models.Model):
    school_id=models.ForeignKey(School,on_delete=models.CASCADE,related_name="teachers")
    teacher_name=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    objects=models.Manager()
    class Meta:
        db_table="teacher_table"



class Student(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="teachers")
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=300)
    Email = models.CharField(max_length=300)
    password = models.CharField(max_length=200)
    marks=models.IntegerField()
    objects=models.Manager()
    class Meta:
        db_table='last'


class Different_Model(models.Model):
    full_name = models.CharField(max_length=200)  
    objects = models.Manager()
    class Meta:
        db_table = 'img_data'



class Enough(models.Model):
    full_id = models.ForeignKey(Different_Model,on_delete=models.CASCADE,related_name="full")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    objects=models.Manager()
    class Meta:
        db_table = "Nested_Json"



###################################################


class User(models.Model):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)  
    objects = models.Manager()
    class Meta:
        db_table = "JWT_TOKEN"

from django.contrib.auth.hashers import make_password, check_password

class Session_Model(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)  
    objects = models.Manager()
    class Meta:
        db_table = "SESSION"



























