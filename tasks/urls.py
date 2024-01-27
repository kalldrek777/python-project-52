from django.urls import path

from .views import *

app_name = 'tasks'

urlpatterns = [
    path('', TaskView.as_view(), name='index_page'),
    path('create/', TaskCreateView.as_view(), name='create_page'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update_page'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_page'),
    path('<int:pk>', TaskDetailView.as_view(), name='detail_page')

]