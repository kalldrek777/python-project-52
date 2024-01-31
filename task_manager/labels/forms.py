from django import forms
from .models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-input'}))

    class Meta:
        model = Label
        fields = ['name']
