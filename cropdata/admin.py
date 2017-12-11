from django.contrib import admin

# Register your models here.
from .models import Pressure, Cropdata
from restapi.models import Info

#myModels = [models.Project, models.Client, models.About]  # iterable list
#admin.site.register(myModels)

admin.site.register(Pressure)
admin.site.register(Cropdata)
admin.site.register(Info)