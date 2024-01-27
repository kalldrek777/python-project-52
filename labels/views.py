from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Label
from .forms import LabelForm


# Create your views here.
class LabelView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/labels.html'
    
    
class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = LabelForm
    model = Label
    template_name = 'users/update.html'
    success_message = "Label is successfully registered"
    success_url = reverse_lazy('labels:index_page')

    def form_valid(self, form):
        form.save()
        return super(LabelCreateView, self).form_valid(form)


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    form_class = LabelForm
    model = Label
    success_message = "Label is changed successfully"
    template_name = "users/update.html"

    def get_success_url(self):
        return reverse_lazy('labels:index_page')


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_message = "Label is deleted successfully"

    def get_success_url(self):
        return reverse_lazy('labels:index_page')