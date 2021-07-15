from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.views.generic import View
from django.views.generic.list import ListView
from django.contrib import messages

from.forms import UserCreateForm, UserEditForm, GroupCreateForm, GroupEditForm


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'accounts/users.html'


class GroupsView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'accounts/groups.html'


class UserCreate(View):
    def get(self, request):
        context = {
            'form': UserCreateForm(),
        }
        return render(request, 'accounts/user_create.html', context)

    def post(self, request):
        if User.objects.filter(username=request.POST['username']).exists():
            messages.error(
                request, 'A user with this username has already been created')
            return redirect('user_create')
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('users')
        else:
            messages.error(
                request, 'Usernames may contain alphanumeric, _, @, +, . and - characters.')
            return redirect('user_create')


class UserEdit(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        context = {
            'form': UserEditForm(instance=user),
            'user': user,
        }
        return render(request, 'accounts/user_edit.html', context)

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully')
        else:
            messages.error(request, 'Error updating user profile')
        return redirect('users')


class UserDelete(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        context = {
            'user': user,
        }
        return render(request, 'accounts/user_delete.html', context)

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('users')


class GroupCreate(View):
    def get(self, request):
        context = {
            'form': GroupCreateForm()
        }
        return render(request, 'accounts/group_create.html', context)

    def post(self, request):
        if Group.objects.filter(name=request.POST['name']).exists():
            messages.error(
                request, 'A group with this name has already been created')
            return redirect('group_create')
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group created successfully')
            return redirect('groups')


class GroupEdit(View):
    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        context = {
            'form': GroupEditForm(instance=group),
            'group': group,
        }
        return render(request, 'accounts/group_edit.html', context)

    def post(self, request, pk):
        group = Group.objects.get(pk=pk)
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Group updated successfully')
        else:
            messages.error(request, 'Error updating group')
        return redirect('groups')


class GroupDelete(View):
    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        context = {
            'group': group,
        }
        return render(request, 'accounts/group_delete.html', context)

    def post(self, request, pk):
        group = Group.objects.get(pk=pk)
        if len(group.user_set.all()) == 0:
            group.delete()
            messages.success(request, 'Group deleted successfully')
        else:
            messages.error(request, 'You cannot delete this group because it has users')

        return redirect('groups')
