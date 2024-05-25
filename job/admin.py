from django.contrib import admin
from .models import Job, Catogery, Apply

# Register your models here.
admin.site.register(Job)
admin.site.register(Catogery)
admin.site.register(Apply)