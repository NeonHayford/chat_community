from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ChannelSerializer, PostSerializer, LikeSerializer
from .models import Channel, Post, Likes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

# Create your views here.
class CreateChannelView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    ordering = ['name']
    search_fields = ['name', 'author']
    def get(self, request):
        try:
            channel = Channel.objects.all()
            serializer = ChannelSerializer(channel, many = True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = ChannelSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateChannelView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, ChannelId, AuthorId):
        try:
            try:
                channel = Channel.objects.get(id=ChannelId, author_id=AuthorId)
            except Channel.DoesNotExist:
                return Response({'message': "Ooops! This channel was not created..."}, status=HTTP_404_NOT_FOUND)
            serializer = ChannelSerializer(channel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, ChannelId, AuthorId):
        try:
            try:
                channel = Channel.objects.get(id=ChannelId, author_id=AuthorId)
            except Channel.DoesNotExist:
                return Response({'message': "Ooops! This channel was not created..."}, status=HTTP_404_NOT_FOUND)
            serializer = ChannelSerializer(channel, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteChannelView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, ChannelId):
        try:
            try:
                channel = Channel.objects.get(id = ChannelId)
            except Channel.DoesNotExist:
                return Response({'message': "Ooops! This channel was not created..."}, status=HTTP_404_NOT_FOUND)
            if Channel.id:
                channel.delete()
                return Response({'success': "Channel was delete successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class CreatePostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    ordering = ['content']
    search_fields = ['content', 'slug']
    def get(self, request):
        try:
            post = Post.objects.all()
            serializer = PostSerializer(post, many = True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = PostSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UpdatePostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, ChannelId, PostId):
        try:
            try:
                post = Post.objects.get(channel_id=ChannelId, id=PostId)
            except Post.DoesNotExist:
                return Response({'message': "Ooops! This channel was not created..."}, status=HTTP_404_NOT_FOUND)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, ChannelId, PostId):
        try:
            try:
                post = Post.objects.get(channel_id=ChannelId, id=PostId)
            except Post.DoesNotExist:
                return Response({'message': "Ooops! This channel was not created..."}, status=HTTP_404_NOT_FOUND)
            serializer = PostSerializer(post, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

class DeletePostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, ChannelId, PostId):
        try:
            try:
                post = Post.objects.get(channel_id=ChannelId, id=PostId)
            except Post.DoesNotExist:
                return Response({'message': "Ooops! This channel was not created..."}, status=HTTP_404_NOT_FOUND)
            if Post:
                post.delete()
                return Response({'success': "image deleted successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


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
                like = Likes.objects.filter(post=post, user=request.user)
                like.delete()
                return Response(status=HTTP_204_NO_CONTENT)
            except Likes.DoesNotExist:
                return Response({'error': 'Ooops! Like not found...'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)