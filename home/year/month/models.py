from django.db import models


class Student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    objects=models.Manager()
    class Meta:
        db_table="house"
