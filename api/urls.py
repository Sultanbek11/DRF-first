from django.urls import path
from .views import (
    my_api_view,
    tasklist_view,
    task_detail_view,
    create_task_view,
    task_update_view,
    task_delete_view,
)

urlpatterns = [
    path('', my_api_view),
    path('tasks/', tasklist_view),
    path('detail/<int:id>', task_detail_view),
    path('create/', create_task_view),
    path('update/<str:id>', task_update_view),
    path('delete/<str:id>', task_delete_view),
]
