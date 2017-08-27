from django.shortcuts import render

from .models import Employee, Teacher
from .serializers import TeacherSerializer, EmployeeSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class EmployeeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)