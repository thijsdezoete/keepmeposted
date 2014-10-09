from django.contrib import admin
from pypi.models import Package, Watcher

# Register your models here.
admin.site.register(Package)
admin.site.register(Watcher)
