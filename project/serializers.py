from rest_framework import serializers
from rest_framework.fields import DateTimeField
from account_app.models import Account, UserProfile
from .models import Team, Task, WeeklyPlan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']



# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = [
#             'id', 'title', 'description', 'assigned_to', 'team', 'status',
#             'start_date', 'end_date', 'depends_on'
#         ]

class TaskSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%Y-%m-%d")
    end_date = serializers.DateField(format="%Y-%m-%d")
    description = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'start_date', 'end_date', 'status', 'created_by',
        ]
        read_only_fields = ['created_by']  # Prevents this field from being updated via the API

    def validate(self, data):
        # Ensure required fields are present
        if 'start_date' not in data or 'end_date' not in data:
            raise serializers.ValidationError({
                "start_date": ["This field is required."],
                "end_date": ["This field is required."],
            })

        # Ensure end_date is after start_date
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({
                "end_date": ["End date must be after start date."]
            })

        return data




class WeeklyPlanSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = WeeklyPlan
        fields = ['id', 'team', 'week_start', 'week_end', 'tasks', 'created_at', 'updated_at']



# class EditableTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'assigned_to', 'team', 'status', 'created_at', 'updated_at']
#         extra_kwargs = {
#             'id': {'read_only': True},
#             'created_at': {'read_only': True},
#             'updated_at': {'read_only': True},
#         }


class EditableTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'depends_on']


class EditableTeamSerializer(serializers.ModelSerializer):
    tasks = EditableTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'tasks']

