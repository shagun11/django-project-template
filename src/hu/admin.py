from django.contrib import admin
from hu import models
# admin.site.register(user)

admin.site.register(models.Movie)
admin.site.register(models.Director)
admin.site.register(models.Genre)
# Register your models her