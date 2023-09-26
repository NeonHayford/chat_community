from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.filters import SearchFilter
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class CreateGroupView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    ordering = ['name']
    search_fields = ['name', 'author']
    def get(self, request):
        try:
            channel = Group.objects.all()
            serializer = GroupSerializer(channel, many = True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = GroupSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateGroupView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, GroupId, AuthorId):
        try:
            try:
                group = Group.objects.get(id=GroupId, author_id=AuthorId)
            except Group.DoesNotExist:
                return Response({'message': "oops! these user-group was not created..."}, status=HTTP_404_NOT_FOUND)
            serializer = GroupSerializer(group, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, GroupId, AuthorId):
        try:
            try:
                group = Group.objects.get(id=GroupId, author_id=AuthorId)
            except Group.DoesNotExist:
                return Response({'message': "oops! this channel was not created..."}, status=HTTP_404_NOT_FOUND)
            serializer = GroupSerializer(group, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)
    # pass

class DeleteGroupView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, GrouplId, AuthorId):
        try:
            try:
                group = Group.objects.get(id=GrouplId,  author_id=AuthorId)
            except Group.DoesNotExist:
                return Response({'message': "oops! this group was not created..."}, status=HTTP_404_NOT_FOUND)
            if group:
                group.delete()
                return Response({'success': "group deleted successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class CreateMessageView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    ordering = ['content']
    search_fields = ['content']
    def get(self, request):
        try:
            message = Message.objects.all()
            serializer = MessageSerializer(message, many = True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = MessageSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteMessageView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, GroupId, MsgId):
        try:
            try:
                msg = Message.objects.get(group_id=GroupId, id=MsgId)
            except Message.DoesNotExist:
                return Response({'message': "oops! message was not created..."}, status=HTTP_404_NOT_FOUND)
            if msg:
                msg.delete()
                return Response({'success': "message was deleted successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class CreateCommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    ordering = ['content']
    search_fields = ['content']
    def get(self, request):
        try:
            comment = Comment.objects.all()
            serializer = CommentSerializer(comment, many = True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = CommentSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteCommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, CommentlId, MessageId):
        try:
            try:
                comment = Comment.objects.get(message_id=MessageId, id=CommentlId)
            except Comment.DoesNotExist:
                return Response({'message': "oops! comment to message was not created..."}, status=HTTP_404_NOT_FOUND)
            if comment:
                comment.delete()
                return Response({'success': "comment was deleted successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class CreateReplyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    ordering = ['message']
    search_fields = ['message']
    def get(self, request):
        try:
            reply = Reply.objects.all()
            serializer = ReplySerializer(reply, many = True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = ReplySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteReplyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, CommentId, ReplyId):
        try:
            try:
                reply = Reply.objects.get(comment_id=CommentId, id=ReplyId)
            except Reply.DoesNotExist:
                return Response({'message': "oops! reply to the comment was not created..."}, status=HTTP_404_NOT_FOUND)
            if Reply:
                reply.delete()
                return Response({'success': "reply was deleted successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        

class MessageLikesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, msg_id):
        try:
            try:
                message = Message.objects.get(id=msg_id)
            except Message.DoesNotExist:
                return Response({'error': 'oops! message was not found...'}, status=HTTP_404_NOT_FOUND)
            like = MsgLikes.objects.create(message=message, user=request.user)
            serializer = MessageLikesSerializer(like)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, msg_id):
        try:
            try:
                message = Message.objects.get(id=msg_id)
            except Message.DoesNotExist:
                return Response({'error': 'Ooops! Message was not found...'}, status=HTTP_404_NOT_FOUND)
            try:
                like = MsgLikes.objects.filter(message=message, user=request.user)
                like.delete()
                return Response({'message':'message likes was removed...'},status=HTTP_204_NO_CONTENT)
            except MsgLikes.DoesNotExist:
                return Response({'error': 'Ooops! Like not found...'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
               
class CommentLikes(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, comment_id):
        try:
            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                return Response({'error': 'oops! comment not found...'}, status=HTTP_404_NOT_FOUND)
            like = CommentLikes.objects.create(comment=comment, user=request.user)
            serializer = CommentLikesSerializer(like)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, comment_id):
        try:
            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                return Response({'error': 'oops! comment was not found...'}, status=HTTP_404_NOT_FOUND)
            try:
                like = CommentLikes.objects.filter(comment=comment, user=request.user)
                like.delete()
                return Response({'message':'comment likes was removed...'}, status=HTTP_204_NO_CONTENT)
            except CommentLikes.DoesNotExist:
                return Response({'error': 'oops! like not found...'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class ReplyLikes(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request, post_id):
        try:
            try:
                post = ReplyLikes.objects.get(id=post_id)
            except ReplyLikes.DoesNotExist:
                return Response({'error': 'ooops! reply was not found...'}, status=HTTP_404_NOT_FOUND)
            like = ReplyLikes.objects.create(post=post, user=request.user)
            serializer = ReplyLikesSerializer(like)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, post_id):
        try:
            try:
                reply = ReplyLikes.objects.get(id=post_id)
            except ReplyLikes.DoesNotExist:
                return Response({'error': 'oops! reply was not found'}, status=HTTP_404_NOT_FOUND)
            try:
                like = ReplyLikes.objects.filter(reply=reply, user=request.user)
                like.delete()
                return Response(status=HTTP_204_NO_CONTENT)
            except ReplyLikes.DoesNotExist:
                return Response({'error': 'oops! like not found...'}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
