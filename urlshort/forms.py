from django import forms 
from .models import Url 

class UrlForm(forms.ModelForm):
	url = forms.URLField(required=True,label = 'لینکتون رو وارد کنید!!',widget=forms.TextInput(attrs={'class':'form-control', 'id':'form1'}))

	class Meta:
		model = Url