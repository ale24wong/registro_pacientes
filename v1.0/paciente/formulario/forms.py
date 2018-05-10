from django import forms

class PacienteForm(forms.Form):
	nombres= forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : ''}))
	apellidos= forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : ''}))
	telefono = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : ''}))