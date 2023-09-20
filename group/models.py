from django.db import models
from  core.settings import AUTH_USER_MODEL
from datetime import datetime
from uuid import uuid4

# Create your models here.
class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    profile = models.ImageField(upload_to='group_profile/')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'group_author')
    members= models.ManyToManyField(AUTH_USER_MODEL, related_name='group_members')
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    community = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    content = models.TextField()
    g_image = models.ImageField(upload_to='msg/images', null=True, blank=True)
    g_video = models.FileField(upload_to='msg/videos', null=True, blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'message_author')
    created_at = models.DateTimeField(auto_now_add= datetime.now())
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def image(self):
        image_data = '{0}'.format(self.image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.video.url)
        return video_data
    
    def __str__(self):
        return self.author


class MsgLikes(models.Model):
    message =models.ForeignKey(Message, on_delete = models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    comment = models.TextField()
    c_image = models.ImageField(upload_to='comment/images', null=True, blank=True)
    c_video = models.FileField(upload_to='comment/videos', null=True, blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_author')
    message = models.ForeignKey(Message, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= datetime.now())
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def image(self):
        image_data = '{0}'.format(self.image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.video.url)
        return video_data


class CommentLikes(models.Model):
    comment =models.ForeignKey(Comment, on_delete = models.CASCADE)
    user = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Reply(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    chat = models.ForeignKey(Comment, on_delete= models.CASCADE)
    message = models.TextField()
    r_image = models.ImageField(upload_to='reply/images', null=True, blank=True)
    r_video = models.FileField(upload_to='reply/videos', null=True, blank=True)
    likes = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    created_at = models.DateTimeField(auto_now_add= datetime.now())
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def image(self):
        image_data = '{0}'.format(self.image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.video.url)
        return video_data


class ReplyLikes(models.Model):
    reply =models.ForeignKey(Reply, on_delete = models.CASCADE)
    user = models.ManyToManyField(AUTH_USER_MODEL, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
