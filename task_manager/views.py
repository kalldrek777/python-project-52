from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from task_manager.users.forms import LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_message = "Вы залогинены"

    def get_success_url(self):
        return reverse_lazy('index_page')


def logout_user(request):
    messages.add_message(request, 20, 'Вы разлогинены')
    logout(request)
    return redirect('index_page')
