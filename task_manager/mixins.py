from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
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


class ObjectUnusedRequaredMixin:
    message_used_object = 'Unable to delete because it is used in task!'
    redirect_url = 'index_page'

    def form_valid(self, form):
        # try:
        #     getattr(self.object, 'is_object_in_use')
        if self.object.is_object_in_use():
            messages.warning(self.request, self.message_used_object)
            return redirect(self.redirect_url)
        return super().form_valid(form)
        # except AttributeError:
        #     messages.warning(self.request, self.message_object_has_not_attr)
        #     return redirect(reverse(self.url_name_object_used))


class AuthorRequaredMixin:
    """ Creator requared (if not - redirect with message). """
    message_not_creator = 'Object is possible to change for its creator only!'
    redirect_url = "index_page"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            object = get_object_or_404(self.model, id=kwargs['pk'])
            if request.user.username != object.get_author_username():
                messages.warning(request, self.message_not_creator)
                return redirect(reverse(self.redirect_url))
        return super().dispatch(request, *args, **kwargs)

