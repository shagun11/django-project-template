from django.contrib import admin
from hu import models
# admin.site.register(user)

admin.site.register(models.Movie)
admin.site.register(models.Director)
admin.site.register(models.Genre)
admin.site.register(models.Rating)
# Register your models her