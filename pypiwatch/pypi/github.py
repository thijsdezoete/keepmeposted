import requests
import base64
from contact import notify_watcher
from models import Package


def check_repo(repo, email=None, subpath='requirements.txt'):
    _base = "https://api.github.com/repos/{repo}/contents/{subpath}"
    url = _base.format(repo=repo, subpath=subpath)
    requirements = requests.get(url).json()
    packages = []
    for p in base64.b64decode(requirements['content']).split("\n"):
        x = p.split('=')
        print x[0], x[-1]
        package, p_created = Package.objects.get_or_create(name=x[0])
        if email:
            notify_watcher(x[0], email)

    return packages


if __name__ == '__main__':
    settings.configure()
    check_repo('thijsdezoete/keepmeposted', 'thijs.dezoete@spilgames.com')

