from django.contrib import admin
from hu.models import Task

# admin.site.register(user)
class TaskAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Task,TaskAdmin)
# Register your models her