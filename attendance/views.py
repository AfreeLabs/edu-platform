from django.shortcuts import render

# Create your views here.
from .models import Attendance
from .serializers import AttendanceSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class AttendanceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
