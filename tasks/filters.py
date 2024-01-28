import django_filters
from django.forms import CheckboxInput

from .models import Task
from labels.models import Label


class TasksFilter(django_filters.FilterSet):

    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        # label=_('Label'),
        queryset=Label.objects.all())

    self_tasks = django_filters.BooleanFilter(
        field_name="author",
        method='logined_user_is_creator_filter',
        label="Show only my tasks",
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