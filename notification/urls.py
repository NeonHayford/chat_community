from django.urls import path, include
from .views import PostNotificationView, MessageNotificationView, CommentNotificationView, ReplyNotificationView

urlpatterns = [
    path('notify/post',  PostNotificationView.as_view()),
    path('notify/msg',  MessageNotificationView.as_view()),
    path('notify/comment',  CommentNotificationView.as_view()),
    path('notify/reply',  ReplyNotificationView.as_view()),
    ]


user.name=NeonHayford
user.email=hayford.lumorvi@amalitech.com
