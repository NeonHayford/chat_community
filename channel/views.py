from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ChannelSerializer, ProfileSerializer, PostSerializer, LikeSerializer
from .models import Channel, Profile, Post, Likes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class ChannelView(APIView):
    pass

class ChannelView(APIView):
    pass

class ChannelView(APIView):
    pass

class LikesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, post_id):
        try:
            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                return Response({'error': 'Ooops! Post not found...'}, status=HTTP_404_NOT_FOUND)
            like = Likes.objects.create(post=post, user=request.user)
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, post_id):
        try:
            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                return Response({'error': 'Ooops! Post not found'}, status=HTTP_404_NOT_FOUND)
            try:
                like = Likes.objects.get(post=post, user=request.user)
                like.delete()
                return Response(status=HTTP_204_NO_CONTENT)
            except Likes.DoesNotExist:
                return Response({'error': 'Ooops! Like not found...'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)