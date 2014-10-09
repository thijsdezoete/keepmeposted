from django.db import models
import requests
from natsort import natsorted

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    version = models.CharField(max_length=25)
    
    def latest_version_known(self):
        version = self.get_versions(latest=True)
        if self.version != version:
            return False
        return True

    def get_version(self, update=False):
        version = self.get_versions(latest=True)
        if self.version != version and update:
            self.version = version
            self.save()
        
        return version

    def get_versions(self, latest=False):
        url = "http://pypi.python.org/pypi/{package_name}/json".format(
                package_name=self.name)
        result = requests.get(url).json()

        # result['info']['version']
        # result['releases']

        if latest:
            return result['info']['version']

        return natsorted(result['releases'].keys())


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Watcher(models.Model):
    email = models.CharField(max_length=300)
    package = models.ForeignKey(Package)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

# TODO: Start using this model:
class PackageWatchers(models.Model):
    watcher = models.ForeignKey(Watcher)
    package = models.ForeignKey(Package)
