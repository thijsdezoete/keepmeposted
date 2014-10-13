from django.core.management.base import BaseCommand, CommandError
from pypi.models import Package, Watcher
from django.core.mail import EmailMessage

class Command(BaseCommand):
    help = 'Checks all packages versions and emails people if updates are available'

    # def add_arguments(self, parser):
    #     parser.add_argument('package', nargs='+', type=int)

    def handle(self, *args, **options):
        for package in Package.objects.all():
            if package.latest_version_known():
                continue
    
            watchers = package.watchers.all()
            mail_text = """{packagename} updated to {version}\n
            Link to changelog: {changelog}
            """.format(
                    packagename=package.name,
                    version=package.get_version(),
                    changelog="test"
            )

            email = EmailMessage(
                    "{pgk} update {vrs}".format(pgk=package.name, vrs=package.get_version()),
                    mail_text, 
                    'noreply@ht5ml.com',
                    ['noreply@ht5ml.com'], 
                    [w.email for w in watchers],
                    headers = {'Reply-To': 'noreply@ht5ml.com'}
            )
            email.send(fail_silently=False)
            package.get_version(update=True)
            
