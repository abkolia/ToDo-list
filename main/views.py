from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, FormView
from .models import TodoModel

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Вход в аккаунт
class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main:list_page')

class RegisterView(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main:list_page')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

class TasksListView(LoginRequiredMixin, ListView):
    model = TodoModel
    queryset = TodoModel.objects.order_by('pk')
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(is_completed=False).count()

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['task_list'] = context['task_list'].filter(task_name__startswith=search_input)

        context['search_input'] = search_input

        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TodoModel
    fields = ['task_name', 'desc', 'is_completed']
    success_url= reverse_lazy('main:list_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = TodoModel
    context_object_name = 'task'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoModel
    fields = ['task_name', 'desc', 'is_completed']
    success_url = reverse_lazy('main:list_page')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoModel
    success_url = reverse_lazy('main:list_page')
