# todo/urls.py

from django.urls import path
from .views import (TodoListView,TodoCreateView,TodoDetailView,TodoUpdateView,TodoDeleteView
)

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
]