from django.db import models
from uuid import uuid4
from core.settings import AUTH_USER_MODEL
from  core import settings
from datetime import datetime

# Create your models here.
class Channel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    author = models.ForeignKey( AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'author')
    members= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

    
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    profile = models.ImageField(upload_to='chat_profile/')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name = 'channel')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.channel.name


class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    channel_content = models.TextField()
    slug = models.SlugField()
    ch_image = models.ImageField(upload_to='post/image', null=True, blank=True)
    ch_video = models.FileField(upload_to='post/video', null=True, blank=True)
    author = models.ForeignKey( AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'post_author')
    created_at = models.DateTimeField(auto_now_add= datetime.now())
    modified_at = models.DateTimeField(auto_now = datetime.now())

    @property
    def image(self):
        image_data = '{0}'.format(self.ch_image.url)
        return image_data
    @property
    def video(self):
        video_data = '{0}'.format(self.ch_video.url)
        return video_data
    

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
