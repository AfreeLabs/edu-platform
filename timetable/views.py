from django.shortcuts import render

# Create your views here.
from .models import Timetable
from .serializers import TimetableSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class TimetableViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)