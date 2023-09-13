from django.urls import path, include
from .views import *


urlpatterns = [
    path('logout', LogoutView.as_view()),
    path('profile/', CreateProfileView.as_view()),
    path('profile/<str:UserId>', updateProfileView.as_view()),
    path('profile/<str:UserId>/delete', DeleteProfileView.as_view()),
]