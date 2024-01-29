from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import StatusForm
from .models import Status
from task_manager.mixins import ObjectUnusedRequaredMixin


# Create your views here.
class StatusView(ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'


class StatusCreateView(SuccessMessageMixin, CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'users/update.html'
    success_message = "Status is successfully registered"
    success_url = reverse_lazy('statuses:index_page')

    def form_valid(self, form):
        form.save()
        return super(StatusCreateView, self).form_valid(form)


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    form_class = StatusForm
    model = Status
    success_message = "Status is changed successfully"
    template_name = "users/update.html"

    def get_success_url(self):
        return reverse_lazy('statuses:index_page')


class StatusDeleteView(ObjectUnusedRequaredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_message = "Status is deleted successfully"
    redirect_url = 'statuses:index_page'

    def get_success_url(self):
        return reverse_lazy('statuses:index_page')
