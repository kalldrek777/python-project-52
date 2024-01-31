from django.urls import path

from .views import (StatusView, StatusCreateView,
                    StatusUpdateView, StatusDeleteView)

app_name = 'statuses'

urlpatterns = [
    path('', StatusView.as_view(), name='index_page'),
    path('create/', StatusCreateView.as_view(), name='create_page'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='update_page'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete_page'),

]
