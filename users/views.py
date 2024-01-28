from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.mixins import LoginRequiredMixin

from .models import CustomUser
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import RegisterForm, LoginForm, UpdateForm


# Create your views here.

class UserView(ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = 'users/users.html'

    def post(self, *args, **kwargs):
        return redirect('index_page')


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = UpdateForm
    model = CustomUser
    success_message = "User is changed successfully"
    # fields = ['first_name', 'second_name', 'username']
    template_name = "users/update.html"

    def get_success_url(self):
        return reverse_lazy('index_page')


class UserDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_message = "User is deleted successfully"

    def get_success_url(self):
        return reverse_lazy('index_page')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_message = "User is successfully registered"
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        form.save()
        return super(UserCreateView, self).form_valid(form)


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index_page')


def logout_user(request):
    logout(request)
    return redirect('login_page')




