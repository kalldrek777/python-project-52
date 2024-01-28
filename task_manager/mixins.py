from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMixin:
    """
    Requared login on dispath.
    If not - returns redirect('login') with message.
    Attrs: message_not_authenticated: str
    """
    message_not_authenticated = 'You are not login. Please, login'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            messages.warning(request, self.message_not_authenticated)
            return redirect(reverse('login_page'))
        return super().dispatch(request, *args, **kwargs)