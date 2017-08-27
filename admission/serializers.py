from admission.models import Registration, Admission 
from rest_framework import serializers

from school.serializers import BatchSerializer
from department.serializers import DepartmentSerializer, ClasslevelSerializer

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Registration
        fields = '__all__'
        extra_fields = ['url']

class AdmissionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    batch = BatchSerializer()
    registree = RegistrationSerializer()
    department = DepartmentSerializer()
    class_level = ClasslevelSerializer()

    class Meta:
        model = Admission
        fields = '__all__'
        extra_fields = ['url']