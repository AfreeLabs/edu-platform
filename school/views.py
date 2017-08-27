from django.shortcuts import render

from .models import School, Batch
from .serializers import SchoolSerializer, BatchSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class SchoolViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)