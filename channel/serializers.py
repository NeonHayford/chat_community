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
    likescounter = serializers.SerializerMethodField('get_likescounter',  read_only=True)
    class Meta:
        model = Likes
        fields = '__all__'


    def get_likescounter(self, request):
        post = request.post
        user = request.user
        likes_count = Likes.objects.filter(post=post, user=user).count()
        return likes_count

