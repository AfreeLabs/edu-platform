from rest_framework import serializers
from .models import School, Batch


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = School
        fields = '__all__'
        extra_fields = ['url']


class BatchSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Batch
        fields = '__all__'
        extra_fields = ['url']

