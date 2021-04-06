from .models import Cidade
from django.forms import ModelForm
from django import forms


class CityForm(ModelForm):
	class Meta:
		model = Cidade
		fields = ['nome']
		widgets = {
			'nome': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})
		}
