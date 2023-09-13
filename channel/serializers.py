from rest_framework.serializers import ModelSerializer
from .models import Channel, Profile, Post, Likes


class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

