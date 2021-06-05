from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(max_length=254, help_text='Required field')
	class Meta:
		model = User
		fields = ['username','email','password']


class UpdateUserForm(forms.ModelForm):
	email = forms.EmailField(max_length=254, help_text='Required field')

	class Meta:
		model = User
		fields = ['email']


class UpdateProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['money','profile_photo']

