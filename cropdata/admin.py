from django.contrib import admin

# Register your models here.
from .models import Pressure, Cropdata, Blog
from restapi.models import Info, Img

#myModels = [models.Project, models.Client, models.About]  # iterable list
#admin.site.register(myModels)

admin.site.register(Pressure)
admin.site.register(Cropdata)
admin.site.register(Info)
admin.site.register(Img)
admin.site.register(Blog)