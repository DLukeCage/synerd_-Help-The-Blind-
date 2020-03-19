from django import forms

class DonationForm(forms.Form):
	Office = forms.CharField(max_length=20)
	Officer = forms.CharField(max_length=20)
	Organization = forms.CharField(max_length=20)
	Organization_Member = forms.CharField(max_length=20)
	Subscriber = forms.CharField(max_length=20)



