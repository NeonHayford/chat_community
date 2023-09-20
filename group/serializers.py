from rest_framework import serializers
from .models import Group, Message, MsgLikes, Comment, CommentLikes, Reply, ReplyLikes

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MsgLikes
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class ReplyLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyLikes
        fields = '__all__'