from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.mixins import LoginRequiredMixin, AuthorRequaredMixin

from .models import CustomUser
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import RegisterForm, UpdateForm


class UserView(ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = 'users/users.html'

    def post(self, *args, **kwargs):
        return redirect('index_page')


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin,
                     AuthorRequaredMixin, UpdateView):
    form_class = UpdateForm
    model = CustomUser
    success_message = "Пользователь успешно изменен"
    message_not_creator = "У вас нет прав для изменения другого пользователя"
    template_name = "users/update.html"
    redirect_url = 'users:index_page'
    extra_context = {
        "button_text": "Изменить"
    }

    def get_success_url(self):
        return reverse_lazy('users:index_page')


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin,
                     AuthorRequaredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_message = "Пользователь успешно удален"
    message_not_creator = "У вас нет прав для изменения другого пользователя"
    redirect_url = 'users:index_page'

    def get_success_url(self):
        return reverse_lazy('users:index_page')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_message = "Пользователь успешно зарегистрирован"
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        form.save()
        return super(UserCreateView, self).form_valid(form)
