from django.urls import path
from .views import TodoListView,TodoDetailView,TodoCreateView,TodoUpdateView,TodoDeleteView



urlpatterns = [
    path('list/', TodoListView.as_view(), name='list'), 
    path('detail/<int:pk>/', TodoDetailView.as_view(), name='detail'), 
    path('create/', TodoCreateView.as_view(), name='create'), 
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'), 
]
