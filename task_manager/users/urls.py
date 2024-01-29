from django.urls import path

from .views import UserView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view(), name='index_page'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_page'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_page'),
    path('create/', UserCreateView.as_view(), name='create_page'),

]