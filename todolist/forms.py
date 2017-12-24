from django import forms
from .models import *
PRIORITY_CHOICES = (
	(0,'Urgent'),
	(1,'Normal'),
)
STATUS_CHOICES = (
	(0,'Unfinished'),
	(1,'finished'),
)
class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields= ['title','end','text','priority']
	def clean_title(self):
		title = self.cleaned_data.get('title')
		if len(title) > 100:
			raise forms.ValidationsError("Length of title should be less than 100.")
		return title
	def clean_end(self):
		end = self.cleaned_data.get('end')
		return end
	def clean_priority(self):
		priority = self.cleaned_data.get('priority')
		return priority
	def clean_text(self):
		text = self.cleaned_data.get('text')
		return text
class AddForm(forms.Form):
 	title = forms.CharField(max_length=100)
	text = forms.CharField()
	createdTime = forms.SplitDateTimeField()
	priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
	finished = forms.ChoiceField(choices=STATUS_CHOICES)

class DeleteForm(forms.Form):
	title=forms.CharField(max_length=100)
	
class EditForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(max_length=200)
class EditTimeForm(forms.Form):
	title = forms.CharField(max_length=100)
	createdTime = forms.SplitDateTimeField()
class EditFinishedForm(forms.Form):
	title = forms.CharField(max_length=100)
	finished = forms.ChoiceField(choices=STATUS_CHOICES)
