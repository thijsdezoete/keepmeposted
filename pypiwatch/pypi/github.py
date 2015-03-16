import requests
import base64

def check_repo(repo, subpath='requirements.txt'):
    _base = "https://api.github.com/repos/{repo}/contents/{subpath}"
    url = _base.format(repo=repo, subpath=subpath)
    requirements = requests.get(url).json()
    for p in base64.b64decode(requirements['content']).split("\n"):
        x = p.split('=')
        print x[0], x[-1]
        yield x[0], x[-1]


if __name__ == '__main__':
    check_repo('thijsdezoete/keepmeposted')

