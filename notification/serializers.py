from rest_framework import serializers
from .models import *
from channel.models import Post

class ChannelNotificationSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField('get_content',  read_only=True)
    class Meta:
        model = ChannelPostNotification
        fields = '__all__'

    def get_content(self, content):
        if self.content is object.__call__():
            call = Post.content.save_form_data()
            assert isinstance(call, content)
            return call


class MessageNotificationSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField('get_content',  read_only=True)    
    class Meta:
        model = GroupMessageNotification
        fields = '__all__'

    def get_content(self, content):
        pass


class CommentNotificationSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField('get_content',  read_only=True)    
    class Meta:
        model = GroupCommentNotification
        fields = '__all__'

    def get_content(self, content):
        pass


class ReplyNotificationSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField('get_content',  read_only=True)    
    class Meta:
        model = GroupReplyNotification
        fields = '__all__'

    def get_content(self, content):
        pass