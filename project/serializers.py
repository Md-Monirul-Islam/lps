# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Team, Task, WeeklyPlan

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']

# class TeamSerializer(serializers.ModelSerializer):
#     members = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = Team
#         fields = ['id', 'name', 'members']

# class TaskSerializer(serializers.ModelSerializer):
#     assigned_to = UserSerializer(read_only=True)
#     team = TeamSerializer(read_only=True)

#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'assigned_to', 'team', 'status', 'created_at', 'updated_at']

# class WeeklyPlanSerializer(serializers.ModelSerializer):
#     team = TeamSerializer(read_only=True)
#     tasks = TaskSerializer(many=True, read_only=True)

#     class Meta:
#         model = WeeklyPlan
#         fields = ['id', 'team', 'week_start', 'week_end', 'tasks', 'created_at', 'updated_at']

