from rest_framework import serializers
from .models import Role, User

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    role_title = serializers.ReadOnlyField(source='role.name')

    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'role_title']