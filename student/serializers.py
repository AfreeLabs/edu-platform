from rest_framework import serializers

from .models import Student, Exam, Grade, Payment
from admission.serializers import AdmissionSerializer
from department.serializers import SubjectSerializer


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    student = AdmissionSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        extra_fields = ['url']


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Exam
        fields = '__all__'
        extra_fields = ['url']


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    exam = ExamSerializer()
    student = StudentSerializer()
    subject = SubjectSerializer()
    class Meta:
        model = Grade
        fields = '__all__'
        extra_fields = ['url']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    student = StudentSerializer()
    class Meta:
        model = Payment
        fields = '__all__'
        extra_fields = ['url']
