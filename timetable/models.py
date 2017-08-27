from django.db import models

import calendar
import datetime


from department.models import ClassLevel
from student.models import Room, Subject
from employee.models import Teacher

# week_days = [(calendar.day_name[0], _(calendar.day_name[0])),
#              (calendar.day_name[1], _(calendar.day_name[1])),
#              (calendar.day_name[2], _(calendar.day_name[2])),
#              (calendar.day_name[3], _(calendar.day_name[3])),
#              (calendar.day_name[4], _(calendar.day_name[4])),
#              (calendar.day_name[5], _(calendar.day_name[5])),
#              (calendar.day_name[6], _(calendar.day_name[6]))]


class Timetable(models.Model):
    name = models.CharField(max_length=64)
    day = models.CharField(max_length=64)
    timing = models.CharField(max_length=32) #like '08AM-10AM' or '8h-10h'
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    




# class Attendance(models.Model):
#     name = models.CharField(max_length=64)
#     classLevel = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)



# class Attendance_sheet(models.Model):
#     name = models.CharField(max_length=64)
#     attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    
