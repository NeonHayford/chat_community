from django.urls import path, include
from .views import *

urlpatterns = [
    # Channels
    path('channel/create',  CreateChannelView.as_view()),
    path('<str:ChannelId>/channel/<str:AuthorId>',  UpdateChannelView.as_view()),
    path('channel/<str:ChannelId>/remove',  DeleteChannelView.as_view()),

    # Posts
    path('post/create',  CreatePostView.as_view()),
    path('channel/<str:ChannelId>/<str:PostId>/remove',  DeletePostView.as_view()),

    # Post likes
    path('post/<str:post_id>/like',  LikesView.as_view()),
    # path('', include('group.urls')),
    path('', include('group.urls')),
]
