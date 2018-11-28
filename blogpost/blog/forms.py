import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms

class RegistrationForm(forms.Form):
	username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class' : 'btn btn-default btn-lg', 'placeholder': 'username'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'btn btn-default btn-lg', 'placeholder': 'e-mail'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'btn btn-default btn-lg', 'placeholder': 'password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'btn btn-default btn-lg', 'placeholder': 'Retype password'}))

	def cleaned_password(self):
		if 'password1' in self.cleaned_data:
			password1 = cleaned_data['password1']
			password2 = cleaned_data['password2']
			if password1 == password2:
				return password2
		raise forms.ValidationError('Password does not match!')

	def cleaned_username(self):
		username = self.cleaned_data['username']
		email = self.cleaned_data['email']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username can only contain alphanumeric and underscore!gogoliii try again!')
		try:
			User.objects.get(email=email)
		except ObjectDoesNotExist:
			raise forms.ValidationError('User already exists!gogoliii try agian!')
