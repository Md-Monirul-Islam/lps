from django.urls import path
from .views import *


urlpatterns = [
    # path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/', TaskListCreateView.as_view(), name='task-create'),
    # path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    # path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/bulk-update/', BulkUpdateStatusView.as_view(), name='task-bulk-update'),

    # Team URLs
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/create/', TeamCreateView.as_view(), name='team-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]

