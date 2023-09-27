from rest_framework.generics import ListCreateAPIView
from .serializers import ChannelNotificationSerializer, MessageNotificationSerializer, CommentNotificationSerializer, ReplyNotificationSerializer
from .models import ChannelPostNotification, GroupMessageNotification, GroupCommentNotification, GroupReplyNotification
from rest_framework.filters import OrderingFilter

# Create your views here.
class PostNotificationView(ListCreateAPIView):
    serializer_class = ChannelNotificationSerializer
    queryset = ChannelPostNotification
    filter_backends = [OrderingFilter]
    ordering = ['sender']
    search_fields = ['sender', 'content']

# Group Context
class MessageNotificationView(ListCreateAPIView):
    serializer_class = MessageNotificationSerializer
    queryset = GroupMessageNotification
    filter_backends = [OrderingFilter]
    ordering = ['sender']
    search_fields = ['sender', 'content']

class CommentNotificationView(ListCreateAPIView):
    serializer_class = CommentNotificationSerializer
    queryset = GroupCommentNotification
    filter_backends = [OrderingFilter]
    ordering = ['sender']
    search_fields = ['sender', 'content']

class ReplyNotificationView(ListCreateAPIView):
    serializer_class = ReplyNotificationSerializer
    queryset = GroupReplyNotification
    filter_backends = [OrderingFilter]
    ordering = ['sender']
    search_fields = ['sender', 'content']

