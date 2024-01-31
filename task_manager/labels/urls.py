from django.urls import path

from .views import LabelView, LabelCreateView, LabelUpdateView, LabelDeleteView

app_name = 'labels'

urlpatterns = [
    path('', LabelView.as_view(), name='index_page'),
    path('create/', LabelCreateView.as_view(), name='create_page'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='update_page'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete_page'),
]
