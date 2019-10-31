from .views import TodoViewSet#, api_root

from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path



todo_list = TodoViewSet.as_view({
    'get':'list',
    'post':'create'
})
todo_detail = TodoViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})


urlpatterns = format_suffix_patterns([
    # path('', api_root),
    path('todo/', todo_list, name='todo-list'),
    path('todo/<int:pk>/', todo_detail, name="todo-detail"),
])