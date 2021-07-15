from django.forms import ModelForm
from django.contrib.auth.models import User, Group


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'groups']


class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'groups']


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']


class GroupEditForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'description']
