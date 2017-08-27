from rest_framework import serializers

from .models import Timetable
from department.serializers import ClasslevelSerializer, SubjectSerializer, RoomSerializer

class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class_level = ClasslevelSerializer()
    teacher = serializers.StringRelatedField()
    subject = SubjectSerializer()
    classroom = RoomSerializer()
    class Meta:
        model = Timetable
        fields = '__all__'
        extra_fields = ['url']




