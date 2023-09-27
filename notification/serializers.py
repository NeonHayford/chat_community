# from rest_framework import serializers
# from .models import ChannelPostNotification
# from account.models import UserSerializer
# from channel.serializers import PostSerializer
# from notification_system.api.serializers import NotificationEventDetailSerializer

# class ChannelNotificationSerializer(NotificationEventDetailSerializer):
#     from_user = UserSerializer()
#     to_user = UserSerializer()
#     push_status = PostSerializer(read_only=True)

#     class Meta:
#         model = ChannelPostNotification
#         fields = '__all__'


# class ChannelNotificationSerializer(serializers.Serializer):
#     class Meta:
#         model = ChannelNotification
#         fields = '__all__'