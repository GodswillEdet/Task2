from django.urls import path

from .views import UserDetail, UserList

urlpatterns = [
    path('api/', UserList.as_view(), name='user-list'),
    path('api/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]