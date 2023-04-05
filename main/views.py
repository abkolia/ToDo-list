from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import TodoModel


class TasksListView(ListView):
    model = TodoModel
    queryset = TodoModel.objects.order_by('pk')
    context_object_name = 'task_list'

class TaskCreateView(CreateView):
    model = TodoModel
    fields = '__all__'

    success_url= reverse_lazy('main:list_page')

class TaskDetailView(DetailView):
    model = TodoModel
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = TodoModel
    fields = '__all__'
    success_url = reverse_lazy('main:list_page')

class TaskDeleteView(DeleteView):
    model = TodoModel
    success_url = reverse_lazy('main:list_page')