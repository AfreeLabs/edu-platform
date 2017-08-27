from django.shortcuts import render

from .models import ClassLevel, Department, Room, Subject
from .serializers import ClasslevelSerializer, DepartmentSerializer, RoomSerializer, SubjectSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class ClasslevelViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ClassLevel.objects.all()
    serializer_class = ClasslevelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SubjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
