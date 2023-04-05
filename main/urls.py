from django.urls import path
from .views import TasksListView, TaskCreateView, TaskDetailView

app_name = 'main'

urlpatterns = [
    path('', TasksListView.as_view(), name='list_page'),
    path('create', TaskCreateView.as_view(), name='create_page'),
    path('detail_task/<int:pk>', TaskDetailView.as_view(), name='detail_task')
]