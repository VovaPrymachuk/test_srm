from django.urls import path

from .views import *


urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('users/user_create/', UserCreate.as_view(), name='user_create'),
    path('users/user_edit/<int:pk>/', UserEdit.as_view(), name='user_edit'),
    path('users/user_delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('groups/', GroupsView.as_view(), name='groups'),
    path('groups/group_create/', GroupCreate.as_view(), name='group_create'),
    path('groups/group_edit/<int:pk>/', GroupEdit.as_view(), name='group_edit'),
    path('groups/group_delete/<int:pk>/',
         GroupDelete.as_view(), name='group_delete'),
]
