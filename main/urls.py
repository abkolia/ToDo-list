from django.urls import path
from .views import TasksListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = 'main'

urlpatterns = [
    path('', TasksListView.as_view(), name='list_page'),
    path('create', TaskCreateView.as_view(), name='create_page'),
    path('detail_task/<int:pk>', TaskDetailView.as_view(), name='detail_page'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='update_page'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='delete_page')
]