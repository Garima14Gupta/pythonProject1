from django.shortcuts import render
from .models import User
from .serializers import UserSerializer,UserValidationSerializer
from rest_framework import viewsets
from rest_framework import response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_201_CREATED



# Create your views here.
class Userviewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request_serializer = UserValidationSerializer(data = request.data)
        import pdb;pdb.set_trace()
        if not request_serializer. is_valid():
            return Response(data={'error':request_serializer.errors},status=HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)

