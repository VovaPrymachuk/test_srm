from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.views.generic import View

from.forms import UserCreateForm, UserEditForm, GroupCreateForm, GroupEditForm


def users(request):
    context = {
        'users': User.objects.all(),
        'groups': Group.objects.all(),
    }
    return render(request, 'accounts/users.html', context)


def groups(request):
    context = {
        'groups': Group.objects.all(),
    }
    return render(request, 'accounts/groups.html', context)


class UserCreate(View):
    def get(self, request):
        context = {
            'form': UserCreateForm(),
        }
        return render(request, 'accounts/user_create.html', context)

    def post(self, request):
        if User.objects.filter(username=request.POST['username']).exists():
            return redirect('user_create')
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')


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
        return redirect('users')


class GroupCreate(View):
    def get(self, request):
        context = {
            'form': GroupCreateForm()
        }
        return render(request, 'accounts/group_create.html', context)

    def post(self, request):
        if Group.objects.filter(name=request.POST['name']).exists():
            return redirect('group_create')
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
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

        return redirect('groups')
