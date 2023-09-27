from django.db import models
from core.settings import AUTH_USER_MODEL
from channel.models import Post
from group.models import Group
from datetime import datetime

# Create your models here.
# Channel events
class ChannelPostNotification(models.Model):
    CHOICES = (
        ("comment", "Comment"),
        ("like", "Like"),
        ("post", "Post"),
        ("warning", "Warning"),
        ("public", "Public"),
    )
    content = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_sent_events", null=True)
    recipient = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel_received_events', null=True)
    timestamp = models.DateTimeField(auto_now_add=datetime.now())
    push_status = models.CharField(max_length=30, choices=CHOICES)



# Group events
class GroupMessageNotification(models.Model):
    CHOICES = (
        ("comment", "Comment"),
        ("like", "Like"),
        ("post", "Post"),
        ("warning", "Warning"),
        ("public", "Public"),
    )
    content = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="group_msg_sent_events", null=True)
    recipient = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_msg_received_events', null=True)
    timestamp = models.DateTimeField(auto_now_add=datetime.now())
    push_status = models.CharField(max_length=30, choices=CHOICES)



class GroupCommentNotification(models.Model):
    CHOICES = (
        ("comment", "Comment"),
        ("like", "Like"),
        ("post", "Post"),
        ("warning", "Warning"),
        ("public", "Public"),
    )
    content = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="group_comment_sent_events", null=True)
    recipient = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_comment_received_events', null=True)
    timestamp = models.DateTimeField(auto_now_add=datetime.now())
    push_status = models.CharField(max_length=30, choices=CHOICES)

class GroupReplyNotification(models.Model):
    CHOICES = (
        ("comment", "Comment"),
        ("like", "Like"),
        ("post", "Post"),
        ("warning", "Warning"),
        ("public", "Public"),
    )
    content = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="group_reply_sent_events", null=True)
    recipient = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_reply_received_events', null=True)
    timestamp = models.DateTimeField(auto_now_add=datetime.now())
    push_status = models.CharField(max_length=30, choices=CHOICES)



