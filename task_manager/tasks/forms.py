from django import forms
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label


class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}
                           ))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control'}
                                  ))
    status = forms.ModelChoiceField(label='Статус',
                                    queryset=Status.objects.all()
                                    )
    executor = forms.ModelChoiceField(label='Исполнитель',
                                      queryset=CustomUser.objects.all()
                                      )
    labels = forms.ModelMultipleChoiceField(label='Метки',
                                            queryset=Label.objects.all(),
                                            required=False
                                            )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
