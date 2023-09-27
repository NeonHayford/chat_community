from .models import *
from rest_framework.views import APIView
from rest_framework.status import *
from django.contrib.auth import logout
from rest_framework.response import Response
from .serializers import ProfileSerializer
from core.settings import MEDIA_ROOT
import os
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class LogoutView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def logout(self, request):
        try:
            logout(request)
            return Response({"detail": "successfully logged out."}, status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)


class CreateProfileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request):
        try:
            serializer = ProfileSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_501_NOT_IMPLEMENTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class updateProfileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, UserId):
        try:
            try:
                image = Profile.objects.get(id = UserId)
            except Profile.DoesNotExist:
                return Response({'error': "user profile does not exist..."}, status=HTTP_404_NOT_FOUND)
            serializer = ProfileSerializer(image, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, UserId):
        try:
            try:
                image = Profile.objects.get(id = UserId)
            except Profile.DoesNotExist:
                return Response({'error': "user profile does not exist..."}, status=HTTP_404_NOT_FOUND)
            serializer = ProfileSerializer(image, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e: return Response({'error': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteProfileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def delete(self, request, UserId):
        try:
            try:
                image = Profile.objects.get(id = UserId)
            except Profile.DoesNotExist:
                return Response({'error': "user profile does not exist..."}, status=HTTP_404_NOT_FOUND)
            if Profile.user_image:
                image_path = os.path.join(MEDIA_ROOT, str(Profile.user_image)) #field # Watch for changes(C:\Users\HayfordLumorvi\Desktop\Projects\django_fastapi\uploads/<django.db.models.fields.files.ImageFileDescriptor object at 0x0000027681F0A350>)
                print(image_path)
                if os.path.exists(image_path):
                    os.remove(image_path)
                    image.delete()
                return Response({'success': "image deleted successfully..."}, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    

    