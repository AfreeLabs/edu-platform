from rest_framework import serializers
from .models import Employee, Teacher


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'
        extra_fields = ['url']


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Teacher
        fields = '__all__'
        extra_fields = ['url']

