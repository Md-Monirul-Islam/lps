# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Team(models.Model):
#     name = models.CharField(max_length=100)
#     members = models.ManyToManyField(User, related_name='teams')


# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tasks')
#     status = models.CharField(max_length=20, choices=[
#         ('planned', 'Planned'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('delayed', 'Delayed'),
#     ], default='planned')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    

# class WeeklyPlan(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='weekly_plans')
#     week_start = models.DateField()
#     week_end = models.DateField()
#     tasks = models.ManyToManyField(Task, related_name='weekly_plans')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)