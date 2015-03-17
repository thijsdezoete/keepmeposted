from django.core.mail import EmailMessage
from django.conf import settings

def notify_watcher(package, watcher):
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
            [watcher.email],
            headers = {'Reply-To': 'noreply@ht5ml.com'}
    )
    if not settings.DEBUG:
        email.send(fail_silently=False)
