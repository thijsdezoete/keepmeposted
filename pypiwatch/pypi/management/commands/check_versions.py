from django.core.management.base import BaseCommand, CommandError
from pypi.models import Package, Watcher

class Command(BaseCommand):
    help = 'Checks all packages versions and emails people if updates are available'

    # def add_arguments(self, parser):
    #     parser.add_argument('package', nargs='+', type=int)

    def handle(self, *args, **options):
        for package in Package.objects.all():
            if package.latest_version_known():
                continue
    
            watchers = Watcher.objects.filter(package=package)
            print watchers
            self.stdout.write('Update for: "%s"' % watchers)
        """ TODO: 
        collect emails
        send watchers email
        update latest version with package.get_version() :)
        """

