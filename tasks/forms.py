from django import forms
from .models import Task
from statuses.models import Status
from users.models import CustomUser


class TaskForm(forms.ModelForm):
    # name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # description = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # status = forms.ModelChoiceField(label='Статус', queryset=Status.objects.all())
    # executor = forms.ModelChoiceField(label='Исполнитель', queryset=CustomUser.objects.all())

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            "description": forms.Textarea(attrs={"cols": 40, "rows": 10})
        }
