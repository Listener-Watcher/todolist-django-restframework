from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not "@" in email:
			raise forms.ValidationError("Invalid eamil address, sign up failed.")
		return email