from django.contrib import admin

# Register your models here.
from .models import States,Cities

admin.site.register(States)
admin.site.register(Cities)