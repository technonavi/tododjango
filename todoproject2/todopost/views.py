from django.shortcuts import render
from django.urls import reverse_lazy
from .models import TodoModel
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# ToDoの一覧表示機能
class TodoListView(ListView):
    template_name='list.html'
    model = TodoModel
    paginate_by = 5

# ToDoの詳細表示機能
class TodoDetailView(DetailView):
    template_name='detail.html'
    model = TodoModel

# ToDoの作成機能
class TodoCreateView(CreateView):
    template_name='create.html'
    model = TodoModel
    fields= ('todo',)
    success_url = reverse_lazy('list')

# ToDoの編集機能
class TodoUpdateView(UpdateView):
    template_name='update.html'
    model = TodoModel
    success_url = reverse_lazy('list')

# ToDoの削除機能
class TodoDeleteView(DeleteView):
    template_name='delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')
