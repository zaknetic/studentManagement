from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    checbox = models.BooleanField()

    def __str__(self):
        return f"{self.name}"