from django.db import models


from department.models import ClassLevel
from student.models import Subject, Student

class Attendance(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField()
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    present = models.BooleanField('Present?', default=True)
    remark = models.CharField(max_length=200)
    total_presence = models.IntegerField()
    total_presence = models.IntegerField()

    def __str__(self):
        return (self.name)

