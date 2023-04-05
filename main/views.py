from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import TodoModel


class TasksListView(ListView):
    model = TodoModel
    queryset = TodoModel.objects.all()
    context_object_name = 'task_list'

class TaskCreateView(CreateView):
    model = TodoModel
    fields = '__all__'

    success_url= reverse_lazy('main:list_page')

class TaskDetailView(DetailView):
    model = TodoModel
    context_object_name = 'task'