from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from .models import Profile, UserReport


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    camps = TaggableManager(verbose_name=u'Pasta')
    class Meta:
        model = Profile
        fields = ['image','name','description','wing','camps']


class ReportUserForm(forms.ModelForm):
    class Meta:
        model = UserReport
        fields = ['reason']