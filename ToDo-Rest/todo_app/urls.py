from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.task_list, name='tasks'),
    path('task-detail/<str:pk>/', views.task_detail, name='tasks-detail'),
    path('task-create/', views.task_create, name='tasks-create'),
    path('task-update/<str:pk>/', views.task_update, name='tasks-update'),
    path('task-delete/<str:pk>/', views.task_delete, name='tasks-delete')
]