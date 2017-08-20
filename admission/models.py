import random
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from school.models import Batch, School
from department.models import Department, ClassLevel

SELECT_GENDER = (
        ('male', 'Male'), ('female', 'Female'),(None, 'Select Gender')
        )


class Registration(models.Model):
    """
    Model representing a person(e.g. mohamed jalloh).
    """
    registration_number = models.PositiveIntegerField(default=0)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    genre = models.CharField(max_length=32, choices=SELECT_GENDER)
    nationality = CountryField(blank_label='(select country)')
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=32)
    email = models.CharField(max_length=100, null=True, blank=True)
    id_card_number = models.CharField(max_length=64)
    guardian = models.CharField(max_length=100)
    guardian_adress = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=32)
    guardian_email = models.CharField(max_length=100, null=True, blank=True)
    school_origin = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name, self.first_name)


@receiver(pre_save, sender=Registration)
def increase_registration_number(sender, instance, *args, **kwargs):
    instance.registration_number += 1



class Admission(models.Model):
    student_card_number = models.PositiveIntegerField(default=0)
    date = models.DateField()
    batch = models.ForeignKey(Batch)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    registree = models.OneToOneField(Registration)
    class_level =models.ForeignKey(ClassLevel, on_delete=models.CASCADE)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return (self.registree.first_name)


@receiver(pre_save, sender=Admission)
def generate_student_card(sendder, instance, *args, **kwargs):
    instance.student_card_number = random.randrange(1000, 9000)
