from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import StatusForm
from .models import Status
from task_manager.mixins import (ObjectUnusedRequaredMixin,
                                 LoginRequiredMixin)


class StatusView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'users/update.html'
    success_message = "Статус успешно создан"
    success_url = reverse_lazy('statuses:index_page')
    extra_context = {
        "button_text": "Создать"
    }

    def form_valid(self, form):
        form.save()
        return super(StatusCreateView, self).form_valid(form)


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = StatusForm
    model = Status
    success_message = "Статус успешно изменен"
    template_name = "users/update.html"
    extra_context = {
        "button_text": "Изменить"
    }

    def get_success_url(self):
        return reverse_lazy('statuses:index_page')


class StatusDeleteView(ObjectUnusedRequaredMixin, LoginRequiredMixin,
                       SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_message = "Статус успешно удален"
    message_used_object = ("Невозможно удалить статус, "
                           "потому что он используется")
    redirect_url = 'statuses:index_page'

    def get_success_url(self):
        return reverse_lazy('statuses:index_page')
