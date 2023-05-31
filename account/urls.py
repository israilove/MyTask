from django.urls import path
from .views import UserListView
from . import views


app_name = 'account'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('api/', views.api_view, name='api'),
]