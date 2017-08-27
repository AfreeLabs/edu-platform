from django.db import models

from admission.models import Admission
from department.models import Subject, Room, Department, ClassLevel

class Student(models.Model):
    
    student = models.OneToOneField(Admission, on_delete=models.CASCADE)


    def __str__(self):
        return '%s, department of %s' % (self.student.registree.first_name, self.student.class_level)



class Exam(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return (self.name)


class Grade(models.Model):
    Grade_1 = models.IntegerField()
    Grade_2 = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Payment(models.Model):
    payment_number = models.CharField(max_length=64)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.DecimalField(max_digits=32, decimal_places=2)
    total_paid = models.DecimalField(max_digits=32, decimal_places=2)
    balance = models.DecimalField(max_digits=32, decimal_places=2)

    def __str__(self):
        return (self.payment_number)
