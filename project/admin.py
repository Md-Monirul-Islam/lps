from django.contrib import admin
from .models import Task, Team, WeeklyPlan

# Register your models here.
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(WeeklyPlan)