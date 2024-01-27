from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import TaskForm
from .models import Task
from users.models import CustomUser


# Create your views here.
class TaskView(ListView):
    model = Task
    context_object_name = 'tasks'
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


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_message = "Task is deleted successfully"

    def get_success_url(self):
        return reverse_lazy('tasks:index_page')
