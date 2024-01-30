from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from .forms import TaskForm
from django_filters.views import FilterView
from .models import Task
from .filters import TasksFilter
from task_manager.mixins import AuthorRequaredMixin


# Create your views here.

class TaskView(LoginRequiredMixin, FilterView):
    filterset_class = TasksFilter
    template_name = 'tasks/tasks.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskForm
    model = Task
    template_name = 'users/update.html'
    success_message = "Task is successfully registered"
    success_url = reverse_lazy('tasks:index_page')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    form_class = TaskForm
    model = Task
    success_message = "Task is changed successfully"
    template_name = "users/update.html"

    def get_success_url(self):
        return reverse_lazy('tasks:index_page')


class TaskDeleteView(AuthorRequaredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_message = "Task is deleted successfully"
    redirect_url = 'tasks:index_page'

    def get_success_url(self):
        return reverse_lazy('tasks:index_page')