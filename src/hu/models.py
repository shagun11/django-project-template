from django.db import models
from django.contrib.auth.models import User
 
TASK_STATUS = ((0, "Pending"),
               (1, "Completed"))

class Task(models.Model):
    task_name = models.CharField(max_length=200) 
    task_description = models.CharField(max_length=200)
    task_status = models.IntegerField(choices=TASK_STATUS, default=0)
    
        
    

