from rest_framework import serializers
from .models import Channel, Post, Likes


class ChannelSerializer(serializers.ModelSerializer):
    Profile = serializers.ImageField(required=False)
    class Meta:
        model = Channel
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

