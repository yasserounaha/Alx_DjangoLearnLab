from django.urls import path
from .views import RegisterView, CustomLoginView
from rest_framework.routers import DefaultRouter
from .views import follow_user, unfollow_user
from . import views
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
