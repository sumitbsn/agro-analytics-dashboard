from django.contrib import admin

# Register your models here.
from .models import Pressure, Cropdata, Blog, Comment


#myModels = [models.Project, models.Client, models.About]  # iterable list
#admin.site.register(myModels)

admin.site.register(Blog)
admin.site.register(Comment)
# admin.site.register(Post)
