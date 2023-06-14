from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import RoleSerializer, UserSerializer
from .models import Role, User

# Create your views here.
class RoleListCreateAPIView(ListCreateAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()