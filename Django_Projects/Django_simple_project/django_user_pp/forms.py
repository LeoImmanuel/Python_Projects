from django import forms
from django.contrib.auth.models import User
from django_user_pp.models import UserProfileInfoModel

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('portfolio_site','profile_pic')