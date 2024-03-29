import django_filters
from django.forms import CheckboxInput

from .models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser


class TasksFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label='Статус',
        field_name='status',
        queryset=Status.objects.all()
    )
    executor = django_filters.ModelChoiceFilter(
        label='Исполнитель',
        field_name='executor',
        queryset=CustomUser.objects.all()
    )

    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        label="Метка",
        queryset=Label.objects.all())

    self_tasks = django_filters.BooleanFilter(
        field_name="author",
        method='logined_user_is_creator_filter',
        label="Только свои задачи",
        widget=CheckboxInput(attrs={'checked': False}))

    def logined_user_is_creator_filter(self, queryset, name, value):
        user = self.request.user
        if value:
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = [
            'labels', 'executor', 'status', 'self_tasks'
        ]
