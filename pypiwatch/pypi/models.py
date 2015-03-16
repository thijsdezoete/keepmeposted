from django.db import models
import requests
from natsort import natsorted

class Package(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500, blank=True)
    version = models.CharField(max_length=25, blank=True)
    watchers = models.ManyToManyField('Watcher', through='PackageWatchers')
    
    def latest_version_known(self, version=None):
        _version = self.get_versions(latest=True)
        if self.version != _version or _version != version:
            return False
        return True

    def get_version(self, update=False):
        version = self.get_versions(latest=True)
        if self.version != version and update:
            self.version = version
            self.save()
        
        return version

    def get_versions(self, latest=False):
        # TODO: Make compatible with other origins(self hosted pypi's)
        url = "http://pypi.python.org/pypi/{package_name}/json".format(
                package_name=self.name)
        result = requests.get(url).json()

        if latest:
            return result['info']['version']

        return natsorted(result['releases'].keys())


    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.name

class Watcher(models.Model):
    email = models.CharField(max_length=300)
    packages = models.ManyToManyField('Package', through='PackageWatchers')

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.email


class PackageWatchers(models.Model):
    watcher = models.ForeignKey(Watcher)
    package = models.ForeignKey(Package)

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return "{watcher}->{package}".format(watcher=self.watcher.email, package=self.package.name)

