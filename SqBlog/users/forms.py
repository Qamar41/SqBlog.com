from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from ckeditor_uploader.widgets import  CKEditorUploadingWidget

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()


    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = [ 'email']


class ProfileUpdateForm(forms.ModelForm):
    # profession = forms.CharField(max_length=30)
    # description = forms.CharField(widget = CKEditorUploadingWidget(),max_length=100)
    # address = forms.CharField(max_length=64)
    # whattsapp = forms.CharField(max_length=20)


    class Meta:
        model = Profile

        fields = ['profession','desccription','Address','whattsapp','image']

