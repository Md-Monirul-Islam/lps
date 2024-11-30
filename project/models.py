from django.db import models
from account_app.models import Account, UserProfile

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Account, related_name='teams')



# TASK_CHOICE = (
#     ('planned', 'Planned'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('delayed', 'Delayed'),
# )

# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     assigned_to = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     team = models.ForeignKey('Team', on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, choices=(TASK_CHOICE))
#     start_date = models.DateField()
#     end_date = models.DateField()
#     depends_on = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='dependencies')

#     def __str__(self):
#         return self.title
    

class Task(models.Model):
    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("delayed", "Delayed"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.title


    

class WeeklyPlan(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='weekly_plans')
    week_start = models.DateField()
    week_end = models.DateField()
    tasks = models.ManyToManyField(Task, related_name='weekly_plans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)