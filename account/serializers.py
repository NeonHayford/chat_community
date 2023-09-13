from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import CustomUser, Profile


class UserSerializer(UserCreateSerializer):
    full_name = serializers.CharField(read_only=True)
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'full_name']


class ProfileSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required = False)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'user_image', 'bio', 'created_at']
