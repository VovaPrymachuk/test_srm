from .utils import ObjectCreateMixin, ObjectDeleteMixin, ObjectUpdateMixin
from django.contrib.auth.models import User, Group
from django.views.generic import View
from django.views.generic.list import ListView

from.forms import UserCreateForm, UserEditForm, GroupCreateForm, GroupEditForm


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'accounts/users.html'


class GroupsView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'accounts/groups.html'


class UserCreate(ObjectCreateMixin, View):
    model = User
    form_model = UserCreateForm
    template = 'accounts/user_create.html'
    success_redirect_url = 'users'
    error_redirect_url = 'user_create'
    objects_already_create_error = 'A user with this username has already been created'
    not_valid_form_message = 'Usernames may contain alphanumeric, _, @, +, . and - characters.'


class UserEdit(ObjectUpdateMixin, View):
    model = User
    model_form = UserEditForm
    template = 'accounts/user_edit.html'
    redirect_url = 'users'


class UserDelete(ObjectDeleteMixin, View):
    model = User
    template = 'accounts/user_delete.html'
    redirect_url = 'users'


class GroupCreate(ObjectCreateMixin, View):
    model = Group
    form_model = GroupCreateForm
    template = 'accounts/group_create.html'
    success_redirect_url = 'groups'
    error_redirect_url = 'group_create'
    objects_already_create_error = 'A group with this name has already been created'


class GroupEdit(ObjectUpdateMixin, View):
    model = Group
    model_form = GroupEditForm
    template = 'accounts/group_edit.html'
    redirect_url = 'groups'


class GroupDelete(ObjectDeleteMixin, View):
    model = Group
    template = 'accounts/group_delete.html'
    redirect_url = 'groups'
