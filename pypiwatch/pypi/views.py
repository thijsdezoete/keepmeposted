from django.shortcuts import render_to_response, redirect
from .forms import SubscribeForm
from django.template.context import RequestContext
from .models import PackageWatchers, Watcher, Package

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
    

def submit(request):
    package_form = SubscribeForm(request.POST)
    if request.method != 'POST':
        return redirect('/')
    if not package_form.is_valid():
        return index(request, package_form)
    
    # process data
    email = package_form.cleaned_data.get('email')
    package_name = package_form.cleaned_data.get('package_name')
    watcher, w_created= Watcher.objects.get_or_create(email=email)
    package, p_created = Package.objects.get_or_create(name=package_name)
    if p_created:
        # verify if valid package
        try:
            package.get_version()
        except Exception as e:
            package.delete()
            return index(request)

    PackageWatchers.objects.get_or_create(watcher=watcher, package=package)
    return redirect('/')
