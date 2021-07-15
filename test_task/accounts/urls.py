from django.urls import path

from . import views


urlpatterns = [
    path('', views.users, name='users'),
    path('users/user_create/', views.UserCreate.as_view(), name='user_create'),
    path('users/user_edit/<int:pk>/', views.UserEdit.as_view(), name='user_edit'),
    path('users/user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('groups/', views.groups, name='groups'),
    path('groups/group_create/', views.GroupCreate.as_view(), name='group_create'),
    path('groups/group_edit/<int:pk>/', views.GroupEdit.as_view(), name='group_edit'),
    path('groups/group_delete/<int:pk>/', views.GroupDelete.as_view(), name='group_delete'),
]
