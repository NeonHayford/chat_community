from django.urls import path
from .views import *

urlpatterns = [
    # Group
    path('group/create', CreateGroupView.as_view(), name='group_chat'),
    path('<str:ChannelId>/group/<str:AuthorId>', UpdateGroupView.as_view(), name='update_group'),
    path('group/<str:ChannelId>/remove', DeleteGroupView.as_view(), name='delete_group'),

    # Message
    path('<str:ChannelId>/group/<str:PostId>/msg',  CreateMessageView.as_view(), name='message'),
    path('<str:ChannelId>/group/<str:PostId>/remove/msg',  DeleteMessageView.as_view(), name='delete_message'),

    # Comment
    path('<str:ChannelId>/group/<str:PostId>/comment', CreateCommentView.as_view(), name='comment'),
    path('<str:ChannelId>/group/<str:PostId>/remove/comment', DeleteCommentView.as_view(), name='delete_comment'),

    # Reply
    path('<str:ChannelId>/group/<str:PostId>/reply', CreateReplyView.as_view(), name='reply'),
    path('<str:ChannelId>/group/<str:PostId>/remove/reply', DeleteReplyView.as_view(), name='delete_reply'),

    # Likes system for Groups Structures
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
    # path('', .as_view(), name=''),
]