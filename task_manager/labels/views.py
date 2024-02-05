from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Label
from .forms import LabelForm
from task_manager.mixins import (ObjectUnusedRequaredMixin,
                                 LoginRequiredMixin)


class LabelView(LoginRequiredMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/labels.html'


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    model = Label
    template_name = 'users/update.html'
    success_message = "Метка успешно создана"
    success_url = reverse_lazy('labels:index_page')
    extra_context = {
        "button_text": "Создать"
    }

    def form_valid(self, form):
        form.save()
        return super(LabelCreateView, self).form_valid(form)


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = LabelForm
    model = Label
    success_message = "Метка успешно изменена"
    template_name = "users/update.html"
    extra_context = {
        "button_text": "Изменить"
    }

    def get_success_url(self):
        return reverse_lazy('labels:index_page')


class LabelDeleteView(ObjectUnusedRequaredMixin, LoginRequiredMixin,
                      SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_message = "Метка успешно удалена"
    message_used_object = ("Невозможно удалить метку,"
                           " потому что она используется")
    redirect_url = 'labels:index_page'

    def get_success_url(self):
        return reverse_lazy('labels:index_page')
