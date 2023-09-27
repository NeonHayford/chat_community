# from django.db import models
# from core.settings import AUTH_USER_MODEL
# from channel.models import Channel
# from group.models import Group
# from datetime import datetime

# # Create your models here.
# class ChannelPostNotification(models.Model):
#     from_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_channel_user')
#     to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_channel_user')
#     author = models.ForeignKey(Channel.author, on_delete=models.CASCADE, related_name='notif_channel_author')
#     members = models.ForeignKey(Channel.members, on_delete=models.CASCADE,related_name='notif_channel_members')
#     pushed_at = models.DateTimeField(auto_now_add=datetime.now())
#     push_status = models.BooleanField(default=False)


# class GroupNotification(models.Model):
#     from_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_group_user')
#     to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_group_user')
#     author = models.ForeignKey(Channel.author, on_delete=models.CASCADE, related_name='notif_group_author')
#     members = models.ForeignKey(Channel.members, on_delete=models.CASCADE, related_name='notif_group_members')
#     pushed_at = models.DateTimeField(auto_now_add=datetime.now())
#     push_status = models.BooleanField(default=False)

