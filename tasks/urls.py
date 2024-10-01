from django.urls import path
from .views import (
    task_list, task_create, task_edit, task_delete,
    category_list, category_create, category_edit, category_delete
)

from .views import signup

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('categories/', category_list, name='category_list'),
    path('category/new/', category_create, name='category_create'),
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
    path('signup/', signup, name='signup'),  # Add this line
]
