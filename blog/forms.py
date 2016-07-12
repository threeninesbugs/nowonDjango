from django import forms

class ContactForm(forms.Form):
	content = forms.CharField(required=True, label='your code', widget=forms.Textarea)