from django.urls import path, include
from .views import *

urlpatterns = [
    # Channels
    path('channel/create',  CreateChannelView.as_view()),
    path('<str:ChannelId>/channel/<str:AuthorId>',  UpdateChannelView.as_view()),
    path('channel/<str:ChannelId>/remove',  DeleteChannelView.as_view()),

    # Posts
    path('post/create',  CreatePostView.as_view()),
    path('<str:ChannelId>/channel/<str:PostId>',  UpdatePostView.as_view()),
    path('channel/<str:ChannelId>/<str:PostId>/remove',  DeletePostView.as_view()),

    # Post likes
    path('post/<str:post_id>/like',  LikesView.as_view()),
    # path('', include('group.urls')),
    path('', include('group.urls')),
]

# post 081f909a-4e2d-4292-9f42-74c159bd5555

# author e82f6676-625b-4bbe-8b15-5d864e805244