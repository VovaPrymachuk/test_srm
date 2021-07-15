from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from django.contrib.auth.models import User, Group


class UserCreateForm(BSModalModelForm):
    class Meta:
        model = User
        fields = ['username', 'groups']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Username'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control',
                                                'label': 'Select group'})
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'groups']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Username'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control',
                                                'label': 'Select group'})
        }


class GroupCreateForm(BSModalModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Group Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Description'})
        }


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Group Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Description'})
        }
