
from rest_framework import serializers
from .models import Attendance

from department.serializers import ClasslevelSerializer, SubjectSerializer
from student.serializers import StudentSerializer

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class_level = ClasslevelSerializer()
    student = StudentSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'
        extra_fields = ['url']



