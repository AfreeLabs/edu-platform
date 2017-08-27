from django.shortcuts import render

from .models import Student, Exam, Grade, Payment
from .serializers import StudentSerializer, ExamSerializer, GradeSerializer, PaymentSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PaymentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)