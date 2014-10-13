from django.contrib import admin
from pypi.models import Package, Watcher, PackageWatchers

# Register your models here.
admin.site.register(Package)
admin.site.register(Watcher)
admin.site.register(PackageWatchers)
