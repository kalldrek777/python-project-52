from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from task_manager.users.forms import LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_message = "Вы залогинены"

    def get_success_url(self):
        return reverse_lazy('index_page')


class LogoutUser(LogoutView):

    def get_success_url(self):
        messages.add_message(self.request, 20, 'Вы разлогинены')
        return reverse_lazy('index_page')
