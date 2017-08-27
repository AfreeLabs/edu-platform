from django.shortcuts import render

# Create your views here.
from .models import Registration, Admission
from .serializers import RegistrationSerializer, AdmissionSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class AdmissionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)











# class RegistrationView(viewsets.ViewSet):
#     """
#     API endpoint that allows the medication to be viewed or added.
#     """

#     def list(self, request, format=None):
#         registrations = Registration.objects.all()
#         serializer = RegistrationSerializer(registrations, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk = None):
#         if pk is not None:
#             medications = Registation.objects.all().filter(id = pk)
#             if pk is not None:
#                 serializer = RegistrationSerializer(medications, many=True)
#                 return Response(serializer.data)
            
#             return Response({
#                 'status': 'Unauthorized',
#                  'message': 'Email/Password invalid.'
#                  }, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({
#                 'status': 'Unauthorized',
#                  'message': 'Email/Password invalid.'
#                  }, status=status.HTTP_204_NO_CONTENT)