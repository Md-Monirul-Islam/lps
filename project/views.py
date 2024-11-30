from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import EditableTaskSerializer, EditableTeamSerializer, TaskSerializer, TeamSerializer
from .models import Task, Team

# Create Task
# class TaskCreateView(CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         serializer.save()

#     http_method_names = ['get', 'post', 'put', 'delete', 'patch']

# # List All Tasks
# class TaskListView(ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [AllowAny]


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(created_by=self.request.user)
        except serializers.ValidationError as e:
            print("Validation Errors:", e.detail)
            raise  

# Update or Delete Task
class TaskUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


# class TaskListView(ListAPIView):
#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         team_id = self.request.query_params.get('team_id')
#         if team_id:
#             return Task.objects.filter(team_id=team_id)
#         return Task.objects.all()
    

# # class TaskCreateView(CreateAPIView):
# #     """
# #     Create a new task.
# #     """
# #     serializer_class = EditableTaskSerializer
# #     permission_classes = [IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save()

# # class TaskCreateView(CreateAPIView):
# #     serializer_class = EditableTaskSerializer
# #     permission_classes = [IsAuthenticated]

# #     def perform_create(self, serializer):
# #         # Attach the currently logged-in user to the task
# #         serializer.save(created_by=self.request.user)

# class TaskCreateView(CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save()


# class TaskDetailView(RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update, or delete a specific task.
#     """
#     serializer_class = EditableTaskSerializer
#     queryset = Task.objects.all()
#     permission_classes = [IsAuthenticated]


# Optionally, a custom view to handle bulk actions (if needed):
class BulkUpdateStatusView(APIView):
    """
    Custom API endpoint for bulk updating task status.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        task_ids = request.data.get('task_ids', [])
        new_status = request.data.get('status', None)
        if not task_ids or not new_status:
            return Response({"error": "task_ids and status are required fields."}, status=400)

        Task.objects.filter(id__in=task_ids).update(status=new_status)
        return Response({"message": "Tasks updated successfully."})
    


class TeamListView(ListAPIView):
    """
    List all teams.
    """
    serializer_class = EditableTeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]


# class TeamCreateView(CreateAPIView):
#     """
#     Create a new team.
#     """
#     serializer_class = EditableTeamSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save()
class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

class TeamDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific team.
    """
    serializer_class = EditableTeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]


