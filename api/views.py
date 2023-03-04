from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import PostSerializer,UserSerializer
from api.models import User
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions

# Create your views here.

class PostModelViewSet(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=request.User)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            usr=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(usr,many=False)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
