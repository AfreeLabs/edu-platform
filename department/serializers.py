from rest_framework import serializers

from .models import ClassLevel, Department, Room, Subject


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Department
        fields = '__all__'
        extra_fields = ['url']


class ClasslevelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    department = DepartmentSerializer()
    class Meta:
        model = ClassLevel
        fields = '__all__'
        extra_fields = ['url']

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    department = DepartmentSerializer()
    class Meta:
        model = Room
        fields = '__all__'
        extra_fields = ['url']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class_level = ClasslevelSerializer()
    teacher = serializers.StringRelatedField()
    class Meta:
        model = Subject
        fields = '__all__'
        extra_fields = ['url']
