from .models import Person
from django.forms import ModelForm
from django import forms
import re

class RegisterForm(ModelForm):
	class Meta:
		model = Person
		fields = ['username','email','phone','first_name','last_name','password']

	password = forms.CharField(
    	widget=forms.PasswordInput()
	)

	def clean_username(self):
		username = self.cleaned_data['username']

		try:
			user = Consumer.objects.get(username=username)
		except:
			return username
		raise forms.ValidationError(u'Username "%s" is already in use.' % username)

	def clean_email(self):
		email = self.cleaned_data['email']

		try:
			email= Consumer.objects.get(email=email)
		except:
			return email
		raise forms.ValidationError('email already registered')


	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password)<6:
			raise forms.ValidationError('Password must be minimum 6 charactors')
		if re.search('[0-9]',password) is None:
			raise forms.ValidationError('Password must be contain at least 1 number')
		if re.search('[A-Z]',password) is None:  
			raise forms.ValidationError('Password must be contain at least 1 capital letter')

		return password


class LoginForm(forms.Form):
	username = forms.CharField(required=True, max_length= 100,
								widget = forms.TextInput(
								attrs = {
										'type' : 'text',
										})
								)
	password = forms.CharField(required=True, widget = forms.PasswordInput(
				attrs={
		                'type': 'password',
		                
		            }))
					



