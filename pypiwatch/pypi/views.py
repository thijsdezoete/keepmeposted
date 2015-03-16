from django.shortcuts import render_to_response, redirect
from .forms import SubscribeForm
from django.template.context import RequestContext
from .models import PackageWatchers, Watcher, Package
from .github import check_repo
import contact

# Create your views here.
def index(request, form=None):
    packages = Package.objects.all()

    subscription = form if form else SubscribeForm
    return render_to_response(
            'index.html', 
            {'packages': packages,
             'subscription_form': subscription
            },
            context_instance=RequestContext(request)
    )
    

def thankyou(request, emailid):
    try:
        watcher = Watcher.objects.get(id=emailid)
        packages = watcher.packages.all()
    except Watcher.DoesNotExist:
        return redirect('/')

    subform = SubscribeForm(initial={'email': watcher})
    return render_to_response(
            'thanks.html', 
            {'packages': packages,
             'subscription_form': subform,
            },
            context_instance=RequestContext(request)
    )
    

def submit(request):
    package_form = SubscribeForm(request.POST)
    if request.method != 'POST':
        return redirect('/')
    if not package_form.is_valid():
        return index(request, package_form)
    
    # process data
    email = package_form.cleaned_data.get('email')
    repo_url = package_form.cleaned_data.get('repo_url')
    package_name = package_form.cleaned_data.get('package_name')
    packages = []
    if repo_url:
        print check_repo(repo_url)
        packages = [(x,v) for x,v in check_repo(repo_url)]
    if package_name:
        packages.append((package_name,None))

    print repo_url, package_name
    watcher, w_created= Watcher.objects.get_or_create(email=email)
    for package in packages:
        package_name = package[0]
        package_version = package[1]
        package, p_created = Package.objects.get_or_create(name=package_name)
        if p_created:
            # verify if valid package
            try:
                _v = package.get_version()
                if _v !=package_version:
                    contact.update_contact(package, watcher)
            except Exception as e:
                package.delete()
                return index(request)

        PackageWatchers.objects.get_or_create(watcher=watcher, package=package)
    return redirect('/thankyou/%s/' % watcher.id)
