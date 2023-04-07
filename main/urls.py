from django.urls import path
from .views import TasksListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView
from .views import CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView

app_name = 'main'

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(next_page='main:login_page'), name='logout_page'),
    path('register', RegisterView.as_view(), name='register_page'),
    path('', TasksListView.as_view(), name='list_page'),
    path('create', TaskCreateView.as_view(), name='create_page'),
    path('detail_task/<int:pk>', TaskDetailView.as_view(), name='detail_page'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='update_page'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='delete_page'),
]