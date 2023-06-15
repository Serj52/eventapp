from django import forms

class CreateEvent(forms.Form):
    name = forms.CharField(label='Название организации')